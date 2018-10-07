import sqlite3

db = sqlite3.connect('database.sqlite')

cursor = db.cursor()

cursor.execute('''
    DROP TABLE IF EXISTS riddles;
''')

cursor.execute('''
    DROP TABLE IF EXISTS users;
''')

cursor.execute('''
    DROP TABLE IF EXISTS scores;
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
        user_id INTEGER,
        riddle_id INTEGER,
        correct INTEGER
    );
''')

cursor.execute('''
    INSERT INTO riddles (question, answer)
    VALUES
        ('What is the color','Yellow'), 
        ('Who is the person', 'Lawrence'),
        ('Which is the show', 'hounds'),
        ('There is a house. One enters it blind and comes out seeing. What is it?','School'),
        ('The more you take, the more you leave behind. What am I?','Steps'),
        ('What has a head, a tail, is brown, and has no legs?','Penny'),
        ('What comes once in a minute, twice in a moment, but never in a thousand years?','Letter M'),
        ('David s father has three sons, Snap, Crackle and ?','David'),
        ('What room do ghosts avoid?','Living room'),
        ('When does Christmas come before Thanksgiving?','Dictionary'),
        ('What has many keys, but cannot even open a single door?','Piano'),
        ('What belongs to you, but other people use it more than you?','Your name'),
        ('What is black when you buy it, red when you use it, and gray when you throw it away?','Charcoal'),
        ('Tall I am young, Short I am old, While with life I glow, Wind is my foe. What am I?','Candle'),
        ('What is more useful when it is broken?','Egg'),
        ('Before Mount Everest was discovered, what was the highest mountain on Earth?','Mount Everest'),
        ('Poor people have it. Rich people need it. If you eat it you die. what is it?','Nothing'),
        ('What runs around the whole yard without moving?','Fence'),
        ('What travels around the world but stays in one spot?','Stamp'),
        ('What 7 letter word is spelled the same way backwards and forewords?','Racecar'),
        ('I can be cracked, I can be made. I can be told, I can be played. What am I?','Joke'),
        ('If you have me, you want to share me. If you share me, you have not got me. What am I?','Secret'),
        ('I use my ear to speak and my mouth to hear. What am I?','A phone'),
        ('I have hands, but cannot hold a thing.','Clock'),
        ('I can carry lots of food, but cannot eat anything.','Fridge'),
        ('It can see, but it isn’t an eye. What is it?','Keyhole'),
        ('You cannot come in or go out without me. What am I?','Door'),
        ('What gets wet when drying?','Towel');
''')

cursor.execute('''
    INSERT INTO users (handle, password)
    VALUES
        ('micaela','signorelli'), 
        ('testuser', 'testpass');
''')

# cursor.execute('''
#    INSERT INTO scores (user_id, riddle_id, correct) 
#    VALUES
#        (1, 1, 1), 
#        (1, 2, 0);
# ''')



db.commit()
db.close()