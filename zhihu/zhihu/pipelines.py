# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from zhihu.items import TopiccategoryItem, DetailtopicItem, QUestionItem, ArticleItem, AnswerItem
from zhihu.SQL.sql import Sql


class ZhihuPipeline(object):
    # 把数据写入mysql.
    
    def close_spider(self, spider):
        #爬虫关闭时，关闭数据库
        Sql.close_mysql()
        
    def process_item(self, item, spider):

        if isinstance(item, TopiccategoryItem):
            #存入mysql
            #查重:            
            Sql.insert_topic_category(item['topic_category_url'],item['topic_category_name'],item['topic_category_id'])
        
        if isinstance(item, DetailtopicItem):
            Sql.insert_detail_topic_category(item['topic_category_id'], item['detail_topic_url'], item['detail_topic_name'], item['detail_topic_summary'])

        if isinstance(item, QUestionItem):
            Sql.insert_zhihu_question(item['question_category_name'], item['question_category_id'], item['question_url'], item['question_title'], item['question_id'])
        
        if isinstance(item, ArticleItem):
            Sql.insert_zhihu_article(item['article_category'], item['article_url'], item['article_title'], item['article_author'])

        if isinstance(item, AnswerItem):
            Sql.insert_zhihu_answer(item['answer_category'], item['answer_url'], item['answer_author'], item['answer_comments'], item['answer_likes'])
        
        return item



