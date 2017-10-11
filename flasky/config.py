# -*- coding:utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <liushaocong97@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_COMMENTS_PER_PAGE = 10
    FLASKY_FOLLOWERS_PER_PAGE = 50

    @staticmethod
    def init_app(app):
        pass

class DevelpomentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_POSTS_PER_PAGE = 20
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data-dev.slite')

class TestingConfig(Config):
    TESTING = True

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data-test.slite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data.slite')

config = {
    'development':DevelpomentConfig,
    'testing':TestingConfig,
    'producting':ProductionConfig,
    'default':DevelpomentConfig

}