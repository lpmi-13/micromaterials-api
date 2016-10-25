# -*- coding: utf-8 -*-
from flask import Blueprint, current_app

from krump import route

version = Blueprint('version', __name__)


@route(version, '/version')
def display_version():
    return 'version', dict(version=(current_app.config['VERSION']))
