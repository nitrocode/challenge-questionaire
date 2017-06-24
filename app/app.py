#!/usr/bin/env python
import questions
import json
from random import shuffle
from flask import Flask, render_template, request, flash
import pdb


app = Flask(__name__)
app.config['DEBUG'] = True
qdata = None


@app.route('/')
def index():
    # pdb.set_trace()
    data = get_questions(page=1)
    return render_template('show_entries.html', qdata=data)


def get_questions(page=1):
    """Get the questions and answers and store in a global variable.

    :return: list of JSON documents
    :rtype: list
    """
    global qdata
    page_size = 10
    # g does not persist the global variable for some reason...
    # qdata = getattr(g, '_questions', None)
    if qdata is None:
        # qdata = g._questions = questions.parse()
        qdata = questions.parse()
    try:
        page = int(page)
    except:
        return qdata
    try:
        if page > 0 and page <= len(qdata) / page_size:
            return qdata[(page - 1) * page_size : page * page_size]
    except:
        pass
    return qdata


@app.route('/questions')
@app.route('/questions/')
@app.route('/questions/<int:page>')
def all_questions(page=None):
    """Return all questions by page.

    :param int page: id
    :return:
    :rtype: dict
    """
    questions = get_questions(page=page)
    data = {
        'data': questions,
        'count': len(questions)
    }
    return json.dumps(data)


@app.route('/question/', methods=['POST'], defaults={'qid':-1})
@app.route('/question/<int:qid>', methods=['PUT', 'GET', 'DELETE'])
def question(qid):
    """Get or modify a question.

    :param int qid: question id
    :return: question and answers
    :rtype: str
    """
    global qdata
    questions = get_questions()
    try:
        real_id = int(qid)
    except:
        real_id = 0
    len_questions = len(questions)
    if real_id >= len_questions:
        real_id = len_questions - 1
    # pdb.set_trace()
    # return a question as a JSON object
    if request.method == 'GET':
        # shuffle answers so you have to use math or a calculator
        #ans = [questions[real_id]['answer']] + \
        #       questions[real_id]['distractors']
        #shuffle(ans)
        #json_data = {
        #    'q': questions[real_id]['question'],
        #    'a': ans
        #}
        json_data = questions[real_id]
        # flash('question {} returned'.format(real_id))
        return json.dumps(json_data)
    # insert/modify the question
    elif request.method in ['PUT', 'POST']:
        data = {
            'answer': request.form['answer'],
            'question': request.form['question'],
            'distractors': request.form['distractors'].split(',')
        }
        # modify the question
        if request.method == 'PUT':
            data['id'] = real_id
            questions[real_id] = data
        # insert new question
        else:
            data['id'] = qdata[-1]['id'] + 1
            questions.append(data)
        qdata = questions
        # flash('question {} modified'.format(real_id))
        # return json.dumps(questions[real_id])
        return ''
    # TODO
    elif request.method in ['DELETE']:
        del questions[real_id]
        return ''
    else:
        return '{}'


if __name__ == '__main__':
    app.run()
