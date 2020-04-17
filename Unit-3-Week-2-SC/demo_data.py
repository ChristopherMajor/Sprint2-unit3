import sqlite3


# Open a connection to a new (blank) database file `demo_data.sqlite3`

DB_FILEPATH = 'demo_data.sqlite3'

connection = sqlite3.connect(DB_FILEPATH)

# - Make a cursor, and execute an appropriate `CREATE TABLE` statement to accept
#   the above data (name the table `demo`)

cursor = connection.cursor()

def refresh():
    command = 'DROP TABLE IF EXISTS demo'
    cursor.execute(command)

refresh()

create_table = '''
CREATE TABLE IF NOT EXISTS demo(
        s varchar NOT NULL,
        x integer,
        y integer
); '''

cursor.execute(create_table)

# - Write and execute appropriate `INSERT INTO` statements to add the data (as
#   shown above) to the database

insert='''
    INSERT INTO demo (s,x,y)
    VALUES ('g',3,9),
           ('v',5,9),
           ('f',8,7);
    '''

cursor.execute(insert)

#Count how many rows you have - it should be 3!
query1 = '''
    SELECT count(DISTINCT s)
    FROM demo;
    '''

cursor.execute(query1)
first_result = cursor.fetchall()
print('How many rows?:', first_result)

#How many rows are there where both `x` and `y` are at least 5?
query2 = '''
    SELECT 
        count(DISTINCT x),
        count(DISTINCT y)
    FROM demo
    WHERE x AND y >= 5;
    '''
result2 = cursor.execute(query2).fetchall()
print('How many rows where both x and y are at least 5?:', result2, '2 rows')

#How many unique values of `y` are there
query3 = '''
    SELECT
        count(DISTINCT y)
    FROM demo;
    '''
result3=cursor.execute(query3).fetchall()
print('Unique values of y:', result3)

cursor.close()
connection.commit()