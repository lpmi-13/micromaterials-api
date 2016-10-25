# -*- coding: utf-8 -*-
"""
L{flask.Flask} application customisation.
"""
import logging
from pkgutil import os

from flask import Flask, Blueprint
from flask_environments import Environments

from krump.support.modules import filter_module


def create_app(package_name, package_path, settings_override=None,
               settings='settings.yaml'):
    """
    Create a L{flask.Flask} application with common configuration applied.

    @param package_name: application package name.
    @param package_path: package path to search for blueporints.
    @param settings: the settings per environment in YAML.
    @param settings_override: a dictionary of settings to override.
    @return: the Flask application; never C{None}.
    """

    app = Flask(package_name, instance_relative_config=True)

    env = Environments(app)
    env.from_yaml(os.path.join(os.getcwd(), '', settings))
    app.config.from_object(settings_override)

    logging.basicConfig(level=logging.DEBUG)

    register_blueprints(app, package_name, package_path)

    return app


def register_blueprints(app, package_name, package_path):
    """
    Register all Blueprint instances on the supplied L{flask.Flask} application
    found in all modules for the specified package.

    @param app: the Flask application; must not be C{None}.
    @param package_name: the package name.
    @param package_path: the package path.
    """

    def is_blueprint(item):
        return isinstance(item, Blueprint)

    blueprints = list(filter_module(package_name, package_path, is_blueprint))
    _logger.debug('Registering [%d] blueprints on [%s].', len(blueprints), app)
    for blueprint, module in blueprints:
        _logger.debug('Registering blueprint from [%s] on [%s].',
                      module.__name__, app)
        app.register_blueprint(blueprint, url_prefix=app.config['MOUNT_POINT'])


_logger = logging.getLogger(__name__)
