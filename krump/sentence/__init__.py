# -*- coding: utf-8 -*-

import logging
from flask import Blueprint, request as flask_request

from krump import no_content
from krump import route
from krump.sentence.sentence import get_sentences
from krump.sentence.to_request import to_request_for_sentences as to_request
from krump.support.collections import has_elements

sentence = Blueprint('sentence', __name__)

_logger = logging.getLogger(__name__)


@route(sentence, '/sentence/<string:feature>')
def get_sentence(feature):
    """
    Get sentences that have the specified feature.

    If there are no sentences for the specified feature
    then a 204 NO CONTENT will be returned.

    The feature might be something like `modal`, `apostrophe`,
    or `simple_past`. (Those examples are not exhaustive.)

    :param feature: what type of sentences are to be returned.
    :return: 200 OK application/json, the sentences
    """

    _logger.debug('Getting sentences for [%s].', feature)

    request = to_request(flask_request, feature)
    sentences = get_sentences(request)

    if has_elements(sentences):
        return 'sentence', dict(sentences=sentences)
    else:
        return no_content()
