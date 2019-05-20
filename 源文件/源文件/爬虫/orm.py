import os, django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Movies

# id,name,year,rating,ratingsum,img,tags,summary,genre,country
# movies = pd.read_csv("data/movies.csv")

# print(movies.dtypes)
# print(movies.info())
# print(movies.loc[0])

def do_movies():
	l = 31441

	for i in range(l):
		id = movies.loc[i].id
		nname = movies.loc[i].nname
		year = movies.loc[i].year
		rating = movies.loc[i].rating
		ratingsum = movies.loc[i].ratingsum
		img = movies.loc[i].img
		tags = movies.loc[i].tags
		summary = movies.loc[i].summary
		genre = movies.loc[i].genre
		country = movies.loc[i].country
		# print(str(nname))
		_ = Movies(id,str(nname),year,rating,ratingsum,img,tags,summary,genre,country)
		_.save()
		print(i,'of',l)

from polls.models import Person

# id,name,img,sex,birthday,birthplace,summary
# persons = pd.read_csv("data/person.csv")

# print(persons.info())
# print(persons.loc[0])

def do_persons():
	l = 127859

	for i in range(l):
		id = persons.loc[i].id
		nname = persons.loc[i].nname
		img = persons.loc[i].img
		sex = persons.loc[i].sex
		birthday = persons.loc[i].birthday
		birthplace = persons.loc[i].birthplace
		summary = persons.loc[i].summary
		try:
			_ = Person(id, nname, img, sex, birthday, birthplace, summary)
			_.save()
		except Exception:
			print(birthplace)
			input()
		print(i,'of',l)

