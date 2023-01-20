# from flask import Flask, render_template

# app = Flask(__name__)

# messages = [{'title': 'What is your name?',
#              'content': '___________'},
#             {'title': 'What skills do you normally use at work?',
#              'content': '____________'},
#             {'title': 'What skills would you like to learn?'
#              'content': '____________'},       
#              {'title': 'Time available?'
#              'content': '____________'},       
#             ]

# @app.route('/')
# def index():
#     return render_template('index.html', messages=messages)

from flask import Flask, render_template

app = Flask(__name__)

messages = [{'title': 'Full name',
             'content': 'Answer:'},
            {'title': 'What skills do you normally use at work?',
             'content': 'Answer:'},
             {'title': 'What skills would you like to learn?',
             'content': 'Answer:'},
             {'title': 'Time availability',
             'content': 'Answer:'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)