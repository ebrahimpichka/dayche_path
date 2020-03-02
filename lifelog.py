#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
from datetime import datetime
import sqlite3

conn = sqlite3.connect('dailylog.db')
c = conn.cursor()

# if the the table does not exist already :
#c.execute("""CREATE TABLE log(activity TEXT,`time` NUMERIC);""")
#conn.commit

commands = sys.argv


if commands[1] == '-m':
    commandline = ''
    for i in commands[2:]:
        commandline += i+' '
    time = datetime.today()
    c.execute("INSERT INTO log VALUES (? , ?);" , (commandline, time))
    conn.commit()
    print('Done !')
elif commands[1] == '-l':
    rows = int(commands[2])
    c.execute("SELECT * FROM log;")
    print(c.fetchmany(rows))
    conn.commit()

conn.close()





