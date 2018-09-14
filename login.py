import sqlite3
import time

def login():
    while True:
        handle = input("Please enter your username: ")
        password = input("Please enter your password: ")
        with sqlite3.connect("database.sqlite") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM users WHERE handle = ? AND password = ?")
        cursor.execute(find_user,(handle, password))
        results = cursor.fetchall()
        
        if results:
            for i in results:
                print("Welcome "+ handle)
            return("exit")
        
        else:
            print("Username and password not recognised")
            again = input("Do you want to try again?(y/n): ")
            if again.lower() == "n":
                print("Goodbye")
                time.sleep(1)
                #return("exit")
                break

login()