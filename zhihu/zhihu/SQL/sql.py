#数据库操作


import pymysql
from zhihu import settings

MYSQL_HOST = settings.MYSQL_HOST
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

config = {
    'host': MYSQL_HOST,
    'port': MYSQL_PORT,
    'user': MYSQL_USER,
    'password': MYSQL_PASSWORD,
    'db': MYSQL_DB,
    'charset': 'utf8',
    # 'cursorclass': pymysql.cursors.DictCursor,
    }


connection = pymysql.connect(**config)
cursor = connection.cursor()


class Sql(object):
    """docstring for Sql"""
    
    @classmethod
    def close_mysql(cls):
        cursor.close()
        connection.close()

    @classmethod
    def insert_topic_category(cls, topic_category_url,topic_category_name,topic_category_id):
        sql = 'INSERT INTO topic_category (topic_category_url, topic_category_name, topic_category_id) VALUES ("{}","{}","{}")'.format(topic_category_url,topic_category_name,topic_category_id)
        cursor.execute(sql)  
        connection.commit() #要改变数据库的内容就要commit。

    @classmethod
    def select_topic_category_id(cls, topic_category_id):
        sql = 'SELECT EXISTS(SELECT 1 FROM topic_category WHERE topic_category_id = "{}")'.format(topic_category_id)
        cursor.execute(sql)
        return cursor.fetchall()[0]

    @classmethod
    def insert_detail_topic_category(cls, topic_category_id, detail_topic_url, detail_topic_name, detail_topic_summary):
        sql = 'INSERT INTO detail_topic_category (topic_category_id, detail_topic_url, detail_topic_name, detail_topic_summary) VALUES ("{}","{}","{}","{}")'.format(topic_category_id, detail_topic_url, detail_topic_name, detail_topic_summary)
        cursor.execute(sql)
        connection.commit()

    @classmethod
    def select_detail_topic_name(cls, detail_topic_name):
        sql = 'SELECT EXISTS(SELECT 1 FROM detail_topic_category WHERE detail_topic_name = "{}")'.format(detail_topic_name)
        cursor.execute(sql)
        return cursor.fetchall()[0]

    @classmethod
    def insert_zhihu_question(cls, question_category_name, question_category_id, question_url, question_title, question_id):
        sql = 'INSERT INTO zhihu_question (question_category_name, question_category_id, question_url, question_title, question_id) VALUES ("{}","{}","{}","{}", "{}")'.format(question_category_name, question_category_id, question_url, question_title, question_id)
        cursor.execute(sql)
        connection.commit()

    @classmethod
    def select_zhihu_question_id(cls, question_id):
        sql = 'SELECT EXISTS(SELECT 1 FROM zhihu_question WHERE question_id = "{}")'.format(question_id)
        cursor.execute(sql)
        return cursor.fetchall()[0]

    @classmethod
    def insert_zhihu_article(cls, article_category, article_url, article_title, article_author):
        sql = 'INSERT INTO zhihu_article (article_category, article_url, article_title, article_author) VALUES ("{}","{}","{}","{}")'.format(article_category, article_url, article_title, article_author)
        cursor.execute(sql)
        connection.commit()

    @classmethod
    def select_zhihu_article_url(cls, article_url):
        sql = 'SELECT EXISTS(SELECT 1 FROM zhihu_article WHERE article_url = "{}")'.format(article_url)
        cursor.execute(sql)
        return cursor.fetchall()[0]

    @classmethod
    def insert_zhihu_answer(cls, answer_category, answer_url, answer_author, answer_comments, answer_likes):
        sql = 'INSERT INTO zhihu_answer (answer_category, answer_url, answer_author, answer_comments, answer_likes) VALUES ("{}","{}","{}","{}", "{}")'.format(answer_category, answer_url, answer_author, answer_comments, answer_likes)
        cursor.execute(sql)
        connection.commit()

    @classmethod
    def select_zhihu_answer_url(cls, answer_url):
        sql = 'SELECT EXISTS(SELECT 1 FROM zhihu_answer WHERE answer_url = "{}")'.format(answer_url)
        cursor.execute(sql)
        return cursor.fetchall()[0]