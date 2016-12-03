# -*- coding: utf-8 -*-

from uritemplate import URITemplate
from werkzeug.datastructures import Headers

from cukes import api_path


class SentenceApi(object):
    """
    A helper class to make it easier to call the Krump API
    from step definitions.
    """

    def __init__(self, client, host='localhost', port=5000):
        self.client = client
        self._api_path = api_path(host, port)
        self.headers = Headers(dict(accept='application/json'))

    def get_sentences(self, request):
        expansions = {
            'count': request.get('count', None),
            'max-words': request.get('max_words', None)
        }

        if request.get('feature', None) is not None:
            template = '/sentence{/feature}{?count,max-words}'
            expansions.update(feature=request['feature'])

        elif request.get('word', None) is not None:
            if request.get('pos', None) is not None:
                template = '/sentence/word{/word}/pos{/pos}{?count,max-words}'
                expansions.update(word=request['word'], pos=request['pos'])

            else:
                template = '/sentence/word{/word}{?count,max-words}'
                expansions.update(word=request['word'])

        else:
            raise NotImplementedError()

        endpoint = URITemplate(self._api_path + template)
        url = endpoint.expand(expansions)
        return self.client.get(url, headers=self.headers)


def request_sentence_with(request, **kwargs):
    new_request = {}
    new_request.update(request)
    new_request.update(kwargs)
    return new_request
