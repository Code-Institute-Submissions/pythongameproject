import sqlite3
import time
import sys

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

def newUser():
    found = 0
    while found == 0:
        user_handle = input("Please enter a username: ")
        with sqlite3.connect("database.sqlite") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM users WHERE handle = ?")
        cursor.execute(findUser, [(user_handle)])
        
        if cursor.fetchall():
            print("Username taken, please try again")
        else:
            found = 1
            
    password = input("Please enter your password: ")
    password1 = input("Please reenter your password: ")
    while password !=password1:
        print ("Your passwords didn't match, try again")
        password = input("Please enter your password: ")
        password1 = input("Please reenter your password: ")
    insertData = '''INSERT INTO users(handle,password) 
    VALUES(?,?)'''
    cursor.execute(insertData,[(user_handle),(password)])
    db.commit()

#newUser()
#login()

def menu():
    while True:
        print("Welcome to the Riddle Game")
        menu =('''
        1 - Create new user
        2 - Login 
        3 - Exit\n''')
        
        userChoice = input(menu)
        
        if userChoice == "1":
            newUser()
        
        elif userChoice == "2":
            login()
            
        elif userChoice == "3":
            print("Goodbye")
            sys.exit()
            
        else:
            print("Invalid option")
            
menu()
        
        