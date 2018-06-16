# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TopiccategoryItem(scrapy.Item):
    """docstring for TopicCategoryItem"""
    
    topic_category_url = scrapy.Field()
    topic_category_name = scrapy.Field()
    topic_category_id = scrapy.Field()

class DetailtopicItem(scrapy.Item):

    topic_category_id = scrapy.Field()
    detail_topic_url = scrapy.Field()
    detail_topic_name = scrapy.Field()
    detail_topic_summary = scrapy.Field()

class QUestionItem(scrapy.Item):
    """docstring for QUestionItem"""
    question_category_name = scrapy.Field()
    question_category_id = scrapy.Field()
    question_url = scrapy.Field()
    question_title = scrapy.Field()
    question_id = scrapy.Field()

class ArticleItem(scrapy.Item):
    """docstring for ArticalItem"""
    #专栏
    article_category = scrapy.Field()
    article_url = scrapy.Field()
    article_title = scrapy.Field()
    article_author = scrapy.Field()

class AnswerItem(scrapy.Item):
    """docstring for AnswerItem"""
    answer_url = scrapy.Field()
    answer_author = scrapy.Field()
    answer_comments = scrapy.Field()
    answer_likes = scrapy.Field()
    answer_category = scrapy.Field()