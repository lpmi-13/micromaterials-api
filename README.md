**Words Given**

[![Such Totes!](https://img.shields.io/badge/such-totes-purple.svg)](https://micromaterialsblog.wordpress.com/)

_A REST-ful API For Words & Stuff_

Read Adam's blog post
[here](https://micromaterialsblog.wordpress.com/2016/10/08/scaling-for-the-future-an-api-for-micromaterials/).

# Setup

```bash
$ virtualenv .venv
$ source .venv/Scripts/activate
$ pip install
```

# Running The Application

```bash
$ python wsgi.py
```

# Running The Tests

## Unit Tests

```bash
$ nosetests
```

## Functional Tests

> Note: these tests require a running MongoDB instance.

```bash
$ behave
```

> The MongoDB instance defaults one running on `localhost`
> but you can change this in the `settings.yml` file.

```bash
$ MONGO_URL: '<insert the URL of your MongoDB instance here>'
```

## Layout

* `krump` :: the application source code.
* `test` :: unit tests for the above source code.
* `cukes` :: BDD tests for the application using [Behave](http://pythonhosted.org/behave/).

## Serving from an endpoint

Once the DB is populated and the application is running, endpoint calls can be made like so:
...for sentences with given features (more or less analogous to parts of speech/word classes)
http://(SERVER_IP_ADDRESS)/api/sentence/apostrophe
- to return 10 sentences with apostrophes

other features currently supported are the following:
 - simple_past
 - non_third_person_singular_simple_present
 - third_person_singular_simple_present
 - present_participle
 - past_participle
 - article
 - singular_noun
 - plural_noun
 - wh_determiner
 - comparative_adjective
 - superlative_adjective

...for sentences with specific words
http://(SERVER_IP_ADDRESS)/api/sentence/word/analysis
- to return 10 sentences with the word 'analysis', if they are available
