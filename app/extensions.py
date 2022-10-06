# -*- coding: utf-8 -*-
"""
Flask 扩展
"""
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()
swagger = Swagger()
