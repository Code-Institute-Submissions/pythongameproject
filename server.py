import sqlite3
import os
from flask import Flask, render_template, request
from Riddle import Riddle
# import 'RiddleRepository.py'

app = Flask('riddle me this')

@app.route('/')
def index():
    return render_template('home.html')

# @app.route('/riddle/')

@app.route('/riddle/<int:riddle_id>')
def showRiddle(riddle_id):
    riddle = Riddle(riddle_id)
    return render_template('ask_riddle.html', question=riddle.question, riddle_id = riddle_id)

@app.route('/riddle/<int:riddle_id>', methods=['POST'])
def answerRiddle(riddle_id):
    riddle = Riddle(riddle_id)

# decide if answer is correct
# render button going to the next riddle (if there are any)

    riddle_correct = riddle.checkAnswer(request.form['answer'])
    return render_template('answer_riddle.html', correct = riddle_correct)

@app.route('/riddle/new')
def showNewRiddle():
# display a form with riddle and answer fields
# action="/riddle/new" method="post"
    return render_template('submit_riddle.html')

@app.route('/riddle/new', methods=['POST'])
def saveNewRiddle():
# get input from form (question and answer)
    question = request.form['question']
    answer = request.form['answer']
    riddle= Riddle.store(question, answer)
    return 'Thanks! We will review your riddle! <a href="/riddle/'+ str(riddle.id) + '"> Find it here </a>'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)