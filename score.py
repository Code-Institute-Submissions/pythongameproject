import sqlite3

class Score(object):

    user_id=''
    riddle_id=''
    correct=''
    @staticmethod
    def record(user_id, riddle_id, correct):
        db = sqlite3.connect('database.sqlite')
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO scores (user_id, riddle_id, correct) 
            VALUES
                (?, ?, ?);
        ''', (user_id, riddle_id,correct))
        db.commit()
        return cursor.lastrowid
        
    @staticmethod
    def get_scores_leaderboard():
        cursor = sqlite3.connect('database.sqlite').cursor()
        return cursor.execute('''
            SELECT
                u.handle AS handle,
                COUNT(s.rowid) AS correct_answers
            FROM users AS u
            JOIN scores AS s ON u.rowid = s.user_id
            WHERE s.correct = 1
            GROUP BY u.rowid
            ORDER BY correct_answers DESC
            LIMIT 10;
        ''')
