import sqlite3

db = sqlite3.connect('database.sqlite')

cursor = db.cursor()

cursor.execute('''
    DROP TABLE riddles;
''')

cursor.execute('''
    DROP TABLE users;
''')

cursor.execute('''
    DROP TABLE scores;
''')

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

cursor.execute('''
    INSERT INTO users (handle, password)
    VALUES
        ('micaela','signorelli'), 
        ('testuser', 'testpass');
''')

db.commit()
db.close()