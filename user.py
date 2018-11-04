import sqlite3
import sys
from flask import session


class User(object):
    id = 0
    username = ""
    password = ""

    def __init__(self, user_id=False):
        if user_id:
            with sqlite3.connect("database.sqlite") as db:
                cursor = db.cursor()
            find_user = ("SELECT handle, password, rowid FROM users WHERE rowid = ?")
            cursor.execute(find_user, (user_id,))
            result = cursor.fetchone()
            self.username = result[0]
            self.password = result[1]
            self.id = result[2]

    @staticmethod
    def fromusername(username):
        with sqlite3.connect("database.sqlite") as db:
            cursor = db.cursor()
        find_user = "SELECT rowid FROM users WHERE handle = ?"
        cursor.execute(find_user, (username,))
        result = cursor.fetchone()
        if not result:
            return False
        return User(result[0])

    @staticmethod
    def fromsession():
        print(session.get('logged_in_user_id'), sys.stderr)
        if session.get('logged_in_user_id') is not None:
            print('logged_in_user_id', sys.stderr)
            if bool(session['logged_in_user_id']) == True:
                return User(session['logged_in_user_id'])
        return False

    def checkPassword(self, password):
        if self.password == password:
            return True
        return False

    @staticmethod
    def newUser(username, password):
        if User.fromusername(username):
            return False
        with sqlite3.connect("database.sqlite") as db:
            cursor = db.cursor()
        insertData = '''INSERT INTO users(handle,password)
        VALUES(?,?)'''
        cursor.execute(insertData, [(username), (password)])
        db.commit()
        return User(cursor.lastrowid)
