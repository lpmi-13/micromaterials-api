# -*- coding: utf-8 -*-

from behave import *

from hamcrest import *

use_step_matcher('re')


def assert_status_code(expected_status_code, response):
    assert_that(response.status_code, equal_to(expected_status_code),
                'Unexpected HTTP response status code.')


def assert_status_code_ok(response):
    assert_status_code(200, response)


def assert_status_code_no_content(response):
    assert_status_code(204, response)
