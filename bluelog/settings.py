# -*- coding: utf-8 -*-

import os

# basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MALL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Bluelog QIN', MAIL_USERNAME)

    BLUELOG_EMAIL = os.getenv('BLUELOG_EMAIL')
    BLUELOG_POST_PER_PAGE = 10
    BLUELOG_MANAGE_POST_PER_PAGE = 15
    BLUELOG_COMMENT_PER_PAGE = 15
    # ('theme name', 'display name')
    BLUELOG_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
    BLUELOG_SLOW_QUERY_THRESHOLD = 1

    BLUELOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    BLUELOG_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


# SQLALCHEMY_DATABASE_URI设置为自己本地存在的数据库
# 开发模式
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/blue_blog'


# 测试模式
class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/blue_blog'


# 生产模式
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/blue_blog'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

development_config=DevelopmentConfig()
testing_config=TestingConfig()
producting_config=ProductionConfig()
print(development_config.SQLALCHEMY_DATABASE_URI)
print(testing_config.SQLALCHEMY_DATABASE_URI)
print(producting_config.SQLALCHEMY_DATABASE_URI)
print(development_config.BLUELOG_ALLOWED_IMAGE_EXTENSIONS)
print(testing_config.BLUELOG_ALLOWED_IMAGE_EXTENSIONS)
print(producting_config.BLUELOG_ALLOWED_IMAGE_EXTENSIONS)
print(config['development'].SQLALCHEMY_DATABASE_URI)
print(config['testing'].SQLALCHEMY_DATABASE_URI)
print(config['production'].SQLALCHEMY_DATABASE_URI)


# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))
print(os.path.abspath((os.path.dirname(__file__))))