import sqlite3

db = sqlite3.connect('database.sqlite')

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE riddles (
        question TEXT,
        answer TEXT
    );
''')

cursor.execute('''
    CREATE TABLE users (
        handle TEXT,
        password TEXT
    );
''')

cursor.execute('''
    CREATE TABLE scores (
        riddle_id INTEGER,
        user_handle TEXT,
        correct INTEGER
    );
''')

cursor.execute('''
    INSERT INTO riddles (question, answer)
    VALUES
        ('What is the color','Yellow'), 
        ('Who is the person', 'Lawrence'),
        ('Which is the show', 'hounds');
''')
db.commit()
db.close()