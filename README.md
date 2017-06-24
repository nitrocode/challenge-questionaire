# Description

Tiny Flask app designed to read a file of questions, display in a table, and allows modification of values.

Quick and dirty proof of concept.

## Prerequisites

* python
* virtualenv
* npm
* bower

## Setup

    $ bower install jquery
    $ cp bower_components/jquery/dist/jquery.min.js app/static/
    $ virtualenv env
    $ . env/bin/activate
    (env) $ pip install -r requirements.txt

## Run

    (env) $ python run.py

# Issues

It's possible that there may be stale `pyc` files in the directory that could cause issues. To prevent that, try removing all `pyc` files prior to running the app.

    (env) $ find . -name "*.pyc" -delete

# TODO

## UI

* take the test
* data validation
* answer verification
* better UI of distractors
* 404 page

## Infrastructure

* grunt
* docker
* setup as models.py, views.py, etc setup
* paging for speed
* minification for speed
* sqlite instead of csv
* app logging
* sphinx
