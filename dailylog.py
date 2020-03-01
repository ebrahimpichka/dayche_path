import sqlite3
import sys
import datetime

conn = sqlite3.connect('lifelog.db')

c = conn.cursor()
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS lifelog
             (id integer primary key autoincrement,
              timeOfTask date, msg text)''')


currentDateTime = datetime.datetime.now()

if len(sys.argv) > 1:

    action = sys.argv[1]

    if action == '-m':
        sql_query = ''' INSERT INTO lifelog (timeOfTask, msg) VALUES (?,?); '''
        params = (currentDateTime, sys.argv[2])
        c.execute(sql_query, params)
        #c.execute("INSERT INTO lifelog (timeOfTask, msg) VALUES ('" 
        #+ currentDateTime + "',' " + sys.argv[2] + "')")
        print('DONE!')
        conn.commit()
    elif action == '-l':
        sql_query = 'SELECT * FROM lifelog limit ' + sys.argv[2]  # + ' ORDER BY id DESC'
        print('The last ', sys.argv[2] , ' task(s):')
        for row in c.execute(sql_query):
            print('The task number:' , row[0] ,
            ' @' + row[1] , ' with message:\n' , row[2])
    elif action == '-h':
        print('for add task use -m switch')
        print('for list task use -l <number> switch')
        
    # Save (commit) the changes
else:
    print("Unknown command! -> press -h for help")
conn.close()

