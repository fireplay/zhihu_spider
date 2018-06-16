# -*- coding: utf-8 -*-

#crawl all questions and answers of zhihu.

#先模拟登陆，然后用cookies去爬取.


import scrapy
from scrapy.http import Request, FormRequest
from PIL import Image
from zhihu.items import TopiccategoryItem, DetailtopicItem, QUestionItem, ArticleItem, AnswerItem
import json
from zhihu import settings
import re
from zhihu.SQL.sql import Sql


class ZhihuSpiders(scrapy.Spider):
    """docstring for ZhihuSpiders"""
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/topics']  
    bash_url = 'https://www.zhihu.com'

    def parse(self, response):
        #得到33个大的分类
        topic_item = TopiccategoryItem()

        topic_category = response.xpath('//li[@class="zm-topic-cat-item"]')
        for topic in topic_category:
            topic_category_url = self.bash_url + '/topics' + topic.xpath('a/@href').extract()[0]
            topic_category_name = topic.xpath('a/text()').extract()[0]
            topic_category_id = topic.xpath('@data-id').extract()[0]

            topic_item['topic_category_url'] = topic_category_url
            
            topic_item['topic_category_name'] = topic_category_name
            topic_item['topic_category_id'] = topic_category_id
            if not (Sql.select_topic_category_id(topic_category_id)[0]):
                yield topic_item
            
            data = [
              ('method', 'next'),
              ('params', '{"topic_id":%s,"offset":0,"hash_id":""}' % topic_category_id ),
            ]

            yield FormRequest(
                'https://www.zhihu.com/node/TopicsPlazzaListV2',
                method = "POST" ,
                headers=settings.headers,
                formdata=data,
                callback=self.parse_topic_category_url, 
                meta={'topic_category_id':topic_category_id, 'offset':0, 'topic_category_name':topic_category_name})

    def parse_topic_category_url(self, response):
        #得到大分类下的小分类
        #因为是动态加载的，直接解析只有前面一部分分类，得不到所有的分类，所以需要分析js。
        # results = response.xpath('//div[@class="blk"]/a[1]')
        # for res in results:
        #     print(res)
        #     name = res.xpath('strong/text()').extract()
        #     print(name)
        #
        #以上代码只能得到部分分类。
        #在这里还是不熟练，稍微做了点反爬的，就束手无策了。
       
        detail_item = DetailtopicItem()
        res = response.text
        res = json.loads(res)
        topics = res['msg']
        if (len(topics) > 0):
            for topic in topics:
                url_regex = re.compile('(?<=<a target="_blank" href=").*?(?=">)')
                name_regex = re.compile("(?<=<strong>).*?(?=</strong>)")
                summary_regex = re.compile('(?<=<p>).*?(?=</p>)')
                url = re.findall(url_regex, topic)[0]
                detail_topic_id = url[7:]
                name = re.findall(name_regex, topic)[0]
                try: #不是所有的都有简介
                    summary = re.findall(summary_regex, topic)[0]
                except IndexError as e:
                    summary = ''
                detail_item['detail_topic_url'] = self.bash_url + url + '/hot'
                detail_item['detail_topic_name'] = name
                detail_item['detail_topic_summary'] = summary
                detail_item['topic_category_id'] = response.meta['topic_category_id']
                if not (Sql.select_detail_topic_name(name)[0]):
                    yield detail_item

                question_url = 'https://www.zhihu.com/api/v4/topics/{}/feeds/top_activity?limit=20&offset=20'.format(detail_topic_id)
                yield Request(question_url, callback=self.parse_topic_questions, meta={'detail_topic_name':response.meta['topic_category_name'], 'detail_topic_id':detail_topic_id})

        topic_category_id = response.meta['topic_category_id']
        offset = response.meta['offset']
        offset += 20

        if(len(res['msg']) > 0):
            data = [
              ('method', 'next'),
              ('params', '{"topic_id":%s,"offset":%s,"hash_id":""}' % (topic_category_id, offset)),
            ]

            yield FormRequest(
                'https://www.zhihu.com/node/TopicsPlazzaListV2',
                method = "POST" ,
                headers = settings.headers,
                formdata = data,
                callback = self.parse_topic_category_url, 
                meta = {'topic_category_id':topic_category_id, 'offset':offset, 'topic_category_name':response.meta['topic_category_name']})
        else:
            print('该话题爬取结束')
            print(response.meta['topic_category_name'] , offset)
            
    def parse_topic_questions(self, response):
        #获取每个话题下的问题
        question_item = QUestionItem()
        article_item = ArticleItem()
        bash_url = 'https://www.zhihu.com/question/'
        text = response.text.encode('utf-8').decode('unicode_escape')
        next_url_reg = re.compile('(?<="next": ").*?(?=")')
        next_url = re.findall(next_url_reg, text)[0]
        detail_topic_name = response.meta['detail_topic_name']
        detail_topic_id = response.meta['detail_topic_id']

        #获取问题名称和url
        question_url_reg = re.compile('(?<="question": {).*?(?=})')
        results = re.findall(question_url_reg, text)        
        for res in results:
            title_reg = re.compile('(?<="title": ").*?(?=")')
            id_reg = re.compile('(?<="id": ).*')
            question_title = re.findall(title_reg, res)[0]
            question_id = re.findall(id_reg, res)[0]
            question_url = bash_url + question_id
            question_item['question_category_name'] = detail_topic_name
            question_item['question_category_id'] = detail_topic_id
            question_item['question_title'] = question_title
            question_item['question_id'] = question_id
            question_item['question_url'] = question_url
            #进行查重，如果数据库有这条数据，就不再yield
            if not (Sql.select_zhihu_question_id(question_id)[0]):
                yield question_item
            #访问question页面，得到问题的回答
            answer_url = 'https://www.zhihu.com/api/v4/questions/{}/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=20'.format(question_id)
            yield Request(answer_url, callback=self.parse_topic_answers, meta={'question_title':question_title, 'question_id':question_id})

        #获取专栏文章名称和url
        #因为获取的json类型的数据，可以不用re处理，直接json获取更好，上面获取question的处理并不好
        results = json.loads(response.text)['data']
        for result in results:
            result = result['target']
            if('question' not in result.keys()):
                article_url = result['url']
                article_title = result['title']
                try:
                    article_author = result['author']['name']
                except KeyError:
                    article_author = ''
                article_category = detail_topic_name
                article_item['article_url'] = article_url
                article_item['article_title'] = article_title
                article_item['article_author'] = article_author
                article_item['article_category'] = article_category
                if not (Sql.select_zhihu_article_url(article_url)[0]):
                    yield article_item

        #不停访问，获得其他的question       
        yield Request(next_url, callback=self.parse_topic_questions, meta={'detail_topic_name':detail_topic_name, 'detail_topic_id':detail_topic_id})   
    
    def parse_topic_answers(self, response):
        #获取每个问题下的所有答案       
        answer_item = AnswerItem()
        bash_url = 'https://www.zhihu.com/question/{}/answer/'.format(response.meta['question_id'])
        pre_results = json.loads(response.text)
        next_url = pre_results['paging']['next']
        # print(url)
        results = pre_results['data']
        for result in results:
            try: #可能没有评论，或者评论被关了
                comments = result['comment_count']
            except KeyError:
                comments = 0
            try:#可能没赞
                likes = result['voteup_count']
            except KeyError:
                likes = 0

            answer_author = result['author']['name']
            answer_id = result['id']
            answer_url = bash_url + str(answer_id)
            answer_category = response.meta['question_title']
            

            answer_item['answer_url'] = answer_url
            answer_item['answer_author'] = answer_author
            answer_item['answer_comments'] = comments
            answer_item['answer_likes'] = likes
            answer_item['answer_category'] = answer_category
            if not (Sql.select_zhihu_answer_url(answer_url)[0]):
                yield answer_item
        yield Request(next_url, callback=self.parse_topic_answers, meta={'question_title':response.meta['question_title'], 'question_id':response.meta['question_id']})

