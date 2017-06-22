#!/usr/bin/env python


def parse(file_name="code_challenge_question_dump.csv",
          delimiter='|', skip_header=True,
          headers=['questions', 'answer', 'distractors']):
    """Parse a CSV of questions.

    The CSV should be delimited and the order of data should be
    question, answer, and distractors where the distractors are
    the wrong answers.

    >>> file_name = "code_challenge_question_dump.csv"
    >>> data = parse(file_name)
    >>> print(data[0])
    {
        'answer': -2182,
        'question': 'What is 1754 - 3936?',
        'distractors': [3176, 6529, 6903]
    }

    :param str file_name: path to CSV
    :param bool skip_header: defaults to True
    :param str delimiter: defaults to '|'
    :return: list of JSON documents
    :rtype: list
    """
    all_data = []
    with open(file_name, "rb") as f:
        if skip_header:
            next(f)
        else:
            headers = f.readline().split(delimiter)
        for idx, line in enumerate(f):
            data = line.split(delimiter)
            # foolishly trust data to convert to int
            distractors = [int(d.replace('\r\n', ''))
                           for d in data[2].split(',')]
            # foolishly trust data to convert to int
            json_doc = {
                'id': idx,
                'question': data[0],
                'answer': int(data[1]),
                'distractors': distractors
            }
            all_data.append(json_doc)
    return all_data


if __name__ == "__main__":
    data = parse()
