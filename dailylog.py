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
        message = sys.argv[2]
        sql_query = ''' INSERT INTO lifelog (timeOfTask, msg) VALUES (?,?); '''
        params = (currentDateTime, message)
        c.execute(sql_query, params)
        print('DONE!')
        conn.commit()
    elif action == '-l':
        
        try:
            count = int(sys.argv[2])
        except:
            print("Enter a number for count of outputs, '", sys.argv[2], "' is not a number", sep="")
            sys.exit(1)

        sql_query = ''' SELECT * FROM lifelog ORDER BY timeOfTask DESC limit ? '''
        params = (str(count))
        print('The last ', count , ' task(s):')
        for row in c.execute(sql_query, params):
            print('IN ' + row[1][0:19] , ':\n> ' , row[2], sep="")

    elif action == '-h':
        print('for add task use -m switch')
        print('for list task use -l <number> switch')
        
else:
    print("Unknown command! -> press -h for help")


conn.close()

