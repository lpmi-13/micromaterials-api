# -*- coding: utf-8 -*-


class SentenceRepository(object):
    """
    A helper class to make easier the setting up and tearing down of scenario data.
    """

    def __init__(self, collection):
        self.collection = collection
        self.submissionIndex = 0

    def purge(self):
        self.collection.delete_many({})

    def add(self, sentence):
        self.collection.insert_one(self.to_document(sentence))

    def add_all(self, sentences):
        for s in sentences:
            sentence = s['sentence']
            features = s['features'].split(',')

            if s.get('pos', None) is not None:
                pos = s['pos'].split(',')
                words = [self.to_word_dictionary(word, pos[index]) for index, word in
                         enumerate(sentence.split(' '))]
            else:
                words = map(self.to_word_dictionary, sentence.split(' '))

            self.add({
                'sentence': sentence,
                'features': features,
                'words': words
            })

    def to_document(self, sentence):
        document = {}
        document.update(self.template_document())
        document.update(sentence)
        return document

    def template_document(self):
        self.submissionIndex += 1
        return {
            'sentence': '',
            'dataType': 'text',
            'source': 'test',
            'submissionID': self.submissionIndex,
            'features': [],
            'words': []
        }

    @staticmethod
    def to_word_dictionary(word, pos=None):
        return dict(original=word, lemma=None, pos=pos)
