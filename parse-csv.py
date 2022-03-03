import csv
from unicodedata import category
from sqlalchemy import create_engine, MetaData, Table, insert
import sqlalchemy

engine = create_engine('sqlite:///blog.db')
connection =  engine.connect()
print(engine.table_names())


# get blog talbe
metadata = MetaData()
post_table = Table('post', metadata, autoload=True, autoload_with=engine)
print(repr(post_table))


with open('TechCrunch1.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    print(reader)
    next(reader)
    for row in reader:
        # check whether it contains content
        if row[0] == "" and row[-1] == "":
            pass
        else: 
            print(row)
            post_id =  row[0]
            title = row[1]
            content_link = row[2]
            date_posted = row[3]
            category_id = row[4]
            
            connection.execute(insert(post_table),{"id": post_id, "title": title, "content_link": content_link, "date_posted": date_posted , "category_id": category_id})