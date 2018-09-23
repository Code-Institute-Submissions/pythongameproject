import sqlite3

class User:
    id = 0
    username = ""
    password = ""
    
    def __init__(self, user_id = False):
        if user_id:
            with sqlite3.connect("database.sqlite") as db:
                cursor = db.cursor()
            find_user = ("SELECT handle, password, rowid FROM users WHERE rowid = ?")
            cursor.execute(find_user,(user_id,))
            result = cursor.fetchone()
            self.username = result[0]
            self.password = result[1]
            self.id = result[2]
        
    @staticmethod
    def fromusername(username):
        with sqlite3.connect("database.sqlite") as db:
            cursor = db.cursor()
        find_user = "SELECT rowid FROM users WHERE handle = ?"
        cursor.execute(find_user,(username,))
        result = cursor.fetchone()
        if not result:
            return False
        return User(result[0])

    def checkPassword(self, password):
        if self.password == password:
            return True
        return False