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
def test():
    return render_template('test.html')


@app.route('/edit')
def edit():
    return render_template('edit.html')


def get_questions(page=None):
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
    return json.dumps({
        'data': questions,
        'count': len(questions)
    })


@app.route('/question/',
            methods=['POST'], defaults={'qid':-1})
@app.route('/question/<int:qid>',
            methods=['PUT', 'GET', 'DELETE'])
def question(qid):
    """Get or modify a question.

    :param int qid: question id
    :return: question and answers
    :rtype: str
    """
    global qdata
    tmp_qdata = get_questions()
    try:
        tmp_qdata[int(qid)]
    except:
        qid = 0
    # return a question as a JSON object
    if request.method == 'GET':
        return json.dumps(tmp_qdata[qid])
    # insert/modify the question
    elif request.method in ['PUT', 'POST']:
        data = {
            'answer': request.form['answer'],
            'question': request.form['question'],
            'distractors': request.form.getlist('distractors[]')
        }
        # modify the question
        if request.method == 'PUT':
            data['id'] = qid
            tmp_qdata[qid] = data
            print(tmp_qdata[qid])
        # insert new question
        else:
            data['id'] = tmp_qdata[-1]['id'] + 1
            tmp_qdata.append(data)
    # remove from array
    elif request.method in ['DELETE']:
        del tmp_qdata[qid]
    qdata = tmp_qdata
    return ''


if __name__ == '__main__':
    app.run()
