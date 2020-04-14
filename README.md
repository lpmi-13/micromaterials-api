# Micromaterials API
**Note: this is no longer in production, and exists only as a module for providing
an endpoint for micromaterials to consume**

[![Such Totes!](https://img.shields.io/badge/such-totes-purple.svg)](https://micromaterialsblog.wordpress.com/)

_A REST-ful API For Words & Stuff_

Read Adam's blog post
[here](https://micromaterialsblog.wordpress.com/2016/10/08/scaling-for-the-future-an-api-for-micromaterials/).

# Setup

```bash
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
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

## Serving Sentences

> This next bit assumes that the DB is populated and the application is running.

To get sentences with a specific feature:

```
http://<SERVER_IP_ADDRESS:PORT>/api/sentence/<FEATURE>
```

> Currently _only_ JSON responses are supported: clients _must_ supply an
`ACCEPT` header value of `application/json`.

If there are no sentences with the desired feature in the underlying DB, then a
`204 NO CONTENT` response will be returned.

`FEATURE` might be `apostrophe` -- to get sentences with apostrophes -- or one
of the features listed below.

 - `simple_past`
 - `non_third_person_singular_simple_present`
 - `third_person_singular_simple_present`
 - `present_participle`
 - `past_participle`
 - `article`
 - `singular_noun`
 - `plural_noun`
 - `wh_determiner`
 - `comparative_adjective`
 - `superlative_adjective`

```bash
curl -XGET -H 'Accept: application/json' http://localhost:9000/api/sentence/apostrophe
```
To get sentences with a specific word (if present in the database):

```
http://<SERVER_IP_ADDRESS:PORT>/api/sentence/word/<WORD>
```

The API also supports three query parameters:

 - `count` : the number of sentences to be returned. (Default `10`.)
 - `max-words` : the maximum number of words in sentences returned. (Default `100`.)

 - `skip` : allows paging and returns the next (skip * count) sentences in the response.
