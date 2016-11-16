# -*- coding: utf-8 -*-

from krump.sentence.mongo import get_sentences as sentences_for
from krump.support.collections import pluck


# noinspection PyUnusedLocal
def apostrophe_sentences(request, sentences):
    # TODO
    pass


def get_sentences(request):
    transform = transforms.get(request['feature'], plain_old_sentences)
    sentences = sentences_for(request)
    return transform(request, sentences)


# noinspection PyUnusedLocal
def plain_old_sentences(request, sentences):
    return map(pluck('sentence'), sentences)


transforms = dict(
    # apostrophe=apostrophe_sentences
)
