# -*- coding: utf-8 -*-

import logging

from flask import Blueprint, request as flask_request

from krump import no_content
from krump import route
from krump.sentence.mongo import get_sentences_containing_word as sentences_containing_word
from krump.sentence.mongo import get_sentences_with_feature as sentences_with_feature
from krump.sentence.to_request import to_request_for_sentences as to_request
from krump.support.collections import has_elements

sentence = Blueprint('sentence', __name__)

_logger = logging.getLogger(__name__)


@route(sentence, '/sentence/<string:feature>')
def get_sentence(feature):
    _logger.debug('Getting sentences for [%s].', feature)

    request = to_request(flask_request, feature=feature)
    sentences = sentences_with_feature(request)

    if not has_elements(sentences):
        return no_content()

    return 'sentence', dict(sentences=sentences,
                            feature=request['feature'])


@route(sentence, '/sentence/word/<string:word>')
def get_sentence_containing_word(word):
    _logger.debug('Getting sentences containing [%s].', word)

    request = to_request(flask_request, word=word)
    sentences = sentences_containing_word(request)

    if not has_elements(sentences):
        return no_content()

    return 'sentence', dict(sentences=sentences,
                            word=request['word'])


@route(sentence, '/sentence/word/<string:word>/pos/<string:pos>')
def get_sentence_containing_word_with_pos(word, pos):
    _logger.debug('Getting sentences containing [%s] and [%s].', word, pos)

    request = to_request(flask_request, word=word, pos=pos)
    sentences = sentences_containing_word(request)

    if not has_elements(sentences):
        return no_content()

    return 'sentence', dict(sentences=sentences,
                            word=request['word'],
                            pos=request['pos'])
