import os
from flask import Flask, render_template, request, redirect, url_for, session
from riddle import Riddle
from score import Score
from user import User


app = Flask('riddle me this')
app.secret_key = 'radnisjf'


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def processlogin():
    username = request.form['username']
    password = request.form['password']

# check if the username already exists
    user = User.fromusername(username)
    if user:
        if user.checkPassword(password):
            session['logged_in_user_id'] = user.id
            session['logged_in_username'] = user.username
            return redirect(url_for('index'))
    else:
        user = User.newUser(username, password)
        if user:
            session['logged_in_user_id'] = user.id
            session['logged_in_username'] = user.username
            return redirect(url_for('index'))

    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/riddle/answer')
def showRiddle():
    user = User.fromsession()
    if not user:
        return redirect('/login')

    riddle = Riddle.get_unanswered_riddle_for_user(user)
    if riddle is None:
        return render_template('riddlesover.html')
    return render_template('ask_riddle.html', riddle=riddle, firstAttempt=True)


@app.route('/riddle/<int:riddle_id>', methods=['POST'])
def answerRiddle(riddle_id):
    riddle = Riddle(riddle_id)
    firstAttempt = request.form['first_attempt']
    firstAttempt = True if request.form['first_attempt'] == "True" else False

    riddle_correct = riddle.checkAnswer(request.form['answer'])
    if riddle_correct is False and firstAttempt is True:
        return render_template('ask_riddle.html', riddle=riddle, firstAttempt=False)

    Score.record(session.get('logged_in_user_id'), riddle.id, riddle_correct)

    return render_template('answer_riddle.html', correct=riddle_correct, riddle=riddle)


@app.route('/riddle/new')
def showNewRiddle():

    return render_template('submit_riddle.html')


@app.route('/riddle/new', methods=['POST'])
def saveNewRiddle():
    # get input from form (question and answer)
    question = request.form['question']
    answer = request.form['answer']
    Riddle.store(question, answer)
    return render_template('thankyou.html')


@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html', scores=Score.get_scores_leaderboard())


if __name__ == '__main__':
    host = os.environ.get('IP') if os.environ.get('IP') else '0.0.0.0'
    port = int(os.environ.get('PORT') if os.environ.get('PORT') else 8080)
    debug = bool(os.environ.get('DEBUG') if os.environ.get('DEBUG') else False)

    app.run(host, port, debug)
