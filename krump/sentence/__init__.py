# -*- coding: utf-8 -*-
from flask import Blueprint, request

from krump import route
from krump.sentence.sentence_memory import get_sentences
from krump.sentence.to_request import to_request_for_sentences as to_request

sentence = Blueprint('sentence', __name__)


@route(sentence, '/sentence/<string:inclusion>')
def get_sentence(inclusion):
    req = to_request(request, inclusion)
    return 'sentence', dict(sentences=get_sentences(req))
