import sqlite3
from User import User


class Riddle:

    id = False
    answer = ''
    question = ''

    def __init__(self, riddle_id: int = False):
        if riddle_id:
            db = sqlite3.connect('database.sqlite')
            cursor = db.cursor()
            cursor.execute('''SELECT rowid, question, answer FROM riddles WHERE rowid = ?''', (str(riddle_id)))
            riddle = cursor.fetchone()
            self.id = riddle[0]
            self.answer = riddle[2]
            self.question = riddle[1]
        
        '''
        with open('riddles') as file:
            riddles = file.read().splitlines()

        riddle = riddles[riddle_id - 1]
        riddle = riddle.split('|')
        self.answer = riddle[1]
        self.question = riddle[0]
        '''
    def checkAnswer(self, answer):
        return self.answer.upper() == answer.upper()
        
    @staticmethod
    def store(question, answer):

    # connect to database 
        db = sqlite3.connect('database.sqlite')
    
    # create cursor
        cursor = db.cursor()
    
    # cursor.execute('''INSERT INTO''', ( question, answer )
        cursor.execute('''
            INSERT INTO riddles (question, answer)
            VALUES
                (?, ?);
        ''', (question, answer))
    
    # get the last inserted row id
        riddle_id = cursor.lastrowid
        
    # commit changes to database
        db.commit()
        db.close()# connect to database 
        db = sqlite3.connect('database.sqlite')
    
    # create cursor
        cursor = db.cursor()
    
    # cursor.execute('''INSERT INTO''', ( question, answer )
        cursor.execute('''
            INSERT INTO riddles (question, answer)
            VALUES
                (?, ?);
        ''', (question, answer))
    
    # get the last inserted row id
        riddle_id = cursor.lastrowid
        
    # commit changes to database
        db.commit()
        db.close()
        
        return Riddle(riddle_id) 

    @staticmethod
    def get_unanswered_riddle_for_user(user: User):
        cursor = sqlite3.connect('database.sqlite').cursor()
        results = cursor.execute('''
        SELECT r2.ROWID AS riddle_id
        FROM riddles AS r2
        WHERE r2.ROWID NOT IN (
            SELECT r.ROWID
            FROM riddles AS r
            INNER JOIN scores AS s
                ON s.riddle_id = r.ROWID
                AND s.user_id = ?
                )
        LIMIT 1;
        ''', (user.id,))
        
        riddle = results.fetchone()
        
        if not riddle:
            return None
            
        return Riddle(riddle[0])