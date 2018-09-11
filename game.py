import os
from flask import Flask, render_template
from Riddle import Riddle
# import 'RiddleRepository.py'

app = Flask('riddle me this')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/riddle/<int:riddle_id>')
def showRiddle(riddle_id):
    riddle = Riddle(riddle_id)
    return render_template('ask_riddle.html', question=riddle.question)

@app.route('/riddle/<int:riddle_id>', methods=['POST'])
def answerRiddle(riddle_id):
    riddle = Riddle(riddle_id)

# decide if answer is correct
# render button going to the next riddle (if there are any)
    return 'Answering riddle #' + str(riddle_id)

@app.route('/riddle/new')
def showNewRiddle():
# display a form with riddle and answer fields
# action="/riddle/new" method="post"
    return 'Give us your best riddle!'

@app.route('/riddle/new', methods=['POST'])
def saveNewRiddle():
# save new riddle in storage
    return 'Thanks! We will review your riddle!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True);