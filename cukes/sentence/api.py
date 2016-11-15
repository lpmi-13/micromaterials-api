# -*- coding: utf-8 -*-

from uritemplate import URITemplate
from werkzeug.datastructures import Headers

from cukes import _api_path


class SentenceApi(object):
    """
    A helper class to make it easier to call the Krump API
    from step definitions.
    """

    def __init__(self, client, host='localhost', port=5000):
        self.client = client
        self.endpoint = self.endpoint_for_sentence(_api_path(host, port))
        self.headers = Headers(dict(accept='application/json'))

    def get_sentences(self, feature, count=None, max_words=None):
        url = self.endpoint.expand({
            'feature': feature,
            'count': count,
            'max-words': max_words
        })
        return self.client.get(url, headers=self.headers)

    @staticmethod
    def endpoint_for_sentence(api_path):
        return URITemplate(api_path + '/sentence{/feature}{?count,max-words}')


def request_sentence_with(request, **kwargs):
    new_request = {}
    new_request.update(request)
    new_request.update(kwargs)
    return new_request
