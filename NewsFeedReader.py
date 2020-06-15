
import requests
from bs4 import BeautifulSoup 
import sqlite3


# get RSS page from isna
url = 'https://www.isna.ir/rss'
response = requests.get(url)



# parsing items(news)
soup = BeautifulSoup(response.content , 'xml')
items = soup.findAll('item')



# Connecting to sqlite dataBase and Creating the news table
conn = sqlite3.connect('NewsFeed.db')

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS newsfeed_tbl
             (date text,
              title text,
              description text,
              category text,
              link text,
              image_url text);''')



# getting the dates of the existing news from the database
select_date_query = '''SELECT date FROM newsfeed_tbl;'''
c.execute(select_date_query)
db_dates = c.fetchall()


# Inserting the news to DataBase if it didnt exist already
for item in items:
    news_date = item.pubDate.text
    news_title = item.title.text
    news_description = item.description.text
    news_link = item.link.text
    news_imageurl = item.enclosure['url']
    news_category = item.category.text
    
    
    if (news_date,) not in db_dates:
        insert_query = ''' INSERT INTO newsfeed_tbl (date, title, description, category, link, image_url) VALUES (?,?,?,?,?,?); '''
        params = (news_date,news_title,news_description,news_link,news_imageurl,news_category)
        c.execute(insert_query,params)
        conn.commit()
    else:
        break



# selecting and printing database news
select_query = '''SELECT * FROM newsfeed_tbl;'''
c.execute(select_query)
news_feed = c.fetchall()

for news in news_feed:
    print('date:  ' , news[0])
    print('title:  ' , news[1])
    print('description:  ' , news[2])
    print('link:  ' , news[3])
    print('image url:  ' , news[4])
    print('category:  ' , news[5])
    print('\n -------------------------------------------- \n')






