import sqlite3
import sys
import datetime

conn = sqlite3.connect('lifelog.db')

c = conn.cursor()
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS lifelog
             (id integer primary key autoincrement,
              timeOfTask text, msg text)''')


currentDateTime = datetime.datetime.now()

if len(sys.argv) > 1:
    if sys.argv[1] == '-m':
        c.execute("INSERT INTO lifelog (timeOfTask, msg) VALUES ('" 
        + str(currentDateTime) + "',' " + sys.argv[2] + "')")
        print('DONE!')
        conn.commit()
    elif sys.argv[1] == '-l':
        sql_query = 'SELECT * FROM lifelog limit ' + sys.argv[2]  # + ' ORDER BY id DESC'
        print('The last ', sys.argv[2] , ' task(s):')
        for row in c.execute(sql_query):
            print('The task number:' , row[0] ,
            ' @' + row[1] , ' with message:\n' , row[2])
    elif sys.argv[1] == '-h':
        print('for add task use -m switch')
        print('for list task use -l <number> switch')
        
    # Save (commit) the changes
else:
    print("Unknown command! -> press -h for help")
conn.close()

