# -*- coding: utf-8 -*-

database = dict(
    presentperfect=[
        'I have seen that movie.',
        'I think I have met him once before.',
        'There have been many earthquakes in California.',
        'People have traveled to the Moon.',
        'People have not traveled to Mars.',
        'Have you read the book yet?',
        'Nobody has ever climbed that mountain.'
    ]
)


def get_sentences(request):
    sentences = database[request['feature']]
    if request['maximum_words'] is not None:
        sentences = [sentence for sentence in sentences if
                     len(sentence.split(' ')) <= request['maximum_words']]
    return sentences[:request['count']]
