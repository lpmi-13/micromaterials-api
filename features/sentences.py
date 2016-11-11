# -*- coding: utf-8 -*-

import json

from hamcrest import *
from uritemplate import URITemplate
from werkzeug.datastructures import Headers


def assert_sentences(expected_sentences, response):
    actual_sentences = json.loads(response.data)['sentences']
    assert_that(actual_sentences, only_contains(*expected_sentences))


class SentenceApi(object):
    def __init__(self, client, host='localhost', port=5000):
        self.client = client
        self.endpoint = SentenceApi.sentence_endpoint(host, port)
        self.headers = Headers(dict(accept='application/json'))

    @staticmethod
    def sentence_endpoint(host, port):
        path = ('http://{}:{}/api/sentence'.format(host, port))
        return URITemplate(path + '{/feature}{?count,max-words}')

    def get_sentences(self, feature, count=None, max_words=None):
        url = self.endpoint.expand({
            'feature': feature,
            'count': count,
            'max-words': max_words
        })
        return self.client.get(url, headers=self.headers)


class SentenceRepository(object):
    def __init__(self, collection):
        self.collection = collection
        self.submissionIndex = 0

    def purge(self):
        self.collection.delete_many({})

    def add(self, sentence):
        document = {}
        document.update(self.template_sentence_document())
        document.update(sentence)
        self.collection.insert_one(document)

    def add_all(self, sentences):
        for s in sentences:
            sentence = s['sentence']
            self.add({
                'sentence': sentence,
                'features': s['features'].split(','),
                'words': sentence.split(' ')
            })

    def template_sentence_document(self):
        self.submissionIndex += 1
        return {
            'sentence': '',
            'dataType': 'text',
            'source': 'test',
            'submissionID': self.submissionIndex,
            'features': [],
            'words': []
        }
