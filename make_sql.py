import pandas as pd
from sqlalchemy import create_engine
import pymysql

db = pymysql.connect(host='localhost', user='root', db='douban')
cursor = db.cursor()

# Relationships
sql_create_relationships = 'create table if not exists Relationships(movie_id varchar(20),person_id varchar(20),role varchar(20))'
cursor.execute(sql_create_relationships)
# 设置编码
cursor.execute('alter table Relationships convert  to character set utf8mb4;')
sql_insert_relationships = 'insert into Relationships values (%s,%s,%s)'
relationships_df = pd.read_csv('./share_data/relationships.csv', header=0, encoding='utf-8')

cursor.executemany(sql_insert_relationships, relationships_df.values.tolist())
db.commit()

# person
sql_create_person = 'create table if not exists Person(id varchar(50),name varchar(500),img varchar(200),sex varchar(10),birthday varchar(20),birthplace varchar(300),summary varchar(6000))'
# 设置编码
cursor.execute(sql_create_person)
cursor.execute('alter table Person convert  to character set utf8mb4;')
sql_insert_person = 'insert into Person values (%s,%s,%s,%s,%s,%s,%s)'
person_df = pd.read_csv('./share_data/person.csv', header=0, encoding='utf-8')
person_df.fillna(value=0, inplace=True)
person_df.columns = ['id', 'name', 'img', 'sex', 'birthday', 'birthplace', 'summary']

cursor.executemany(sql_insert_person, person_df.values.tolist())
db.commit()
db.rollback()

# movie
sql_create_movie = 'create table if not exists Movie(id varchar(50),movie_name varchar(500),movie_year varchar(20),rating varchar(10),ratingsum varchar(20),img varchar(200),tags varchar(200),summary varchar(6000),genre varchar(30),country varchar(200))'
# 设置编码
cursor.execute(sql_create_movie)
cursor.execute('alter table Movie convert  to character set utf8mb4;')
sql_insert_movie = 'insert into Movie values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
movie_df = pd.read_csv('./share_data/movies.csv', header=0, encoding='utf-8')
movie_df.fillna(value=0, inplace=True)
movie_df.columns = ['id', 'movie_name', 'movie_year', 'rating', 'ratingsum', 'img', 'tags', 'summary', 'genre',
                    'country']

cursor.executemany(sql_insert_movie, movie_df.values.tolist())
db.commit()
db.rollback()

# comment
sql_create_comment = 'create table if not exists Comment(user_name varchar(50),details varchar(5000),id varchar(20))'
# 设置编码
cursor.execute(sql_create_comment)
cursor.execute('alter table Comment convert  to character set utf8mb4;')
sql_insert_comment = 'insert into Comment values (%s,%s,%s)'
comment_df = pd.read_csv('./share_data/comment.csv', header=None, encoding='utf-8')
comment_df.fillna(value=0, inplace=True)
comment_df.columns = ['user_name', 'details', 'id']

cursor.executemany(sql_insert_comment, comment_df.values.tolist())
db.commit()
db.rollback()

cursor.close()
db.close()
