# -*- coding: utf-8 -*-

import json

from hamcrest import *
from uritemplate import URITemplate
from werkzeug.datastructures import Headers

headers = Headers(dict(accept='application/json'))


def assert_sentences(expected_sentences, response):
    actual_sentences = json.loads(response.data)['sentences']
    assert_that(expected_sentences, only_contains(*actual_sentences))


class SentenceApi(object):
    def __init__(self, client, host='localhost', port=5000):
        self.client = client
        self.endpoint = URITemplate(('http://{}:{}/api/sentence'.format(host, port)) + '{/feature}{?count}')

    def get_sentences(self, feature, count=None):
        url = self.endpoint.expand(feature=feature, count=count)
        return self.client.get(url, headers=headers)


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
            self.add({
                'sentence': s['sentence'],
                'features': s['features'].split(',')
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
