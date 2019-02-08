#based on: https://www.diveinto.org/python3/your-first-python-program.html#importsearchpath
#anaconds search path is apparently incomplete?
import sys
sys.path.insert(0, 'D:\\Downloads\\Anaconda3\\envs\\rangoProj\\Lib\\site-packages')
sys.path.insert(0, 'D:\\PythonWorkspace\\tango_with_django_project')

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page
import random

def populate():
	#First we create lists of dictionaries conainting the pages we want to add
	#to each catagory
	#Then we will create a dictionary of dictionaries for out catagories
	#this allows us to iterate through each datastructure, and add the data to our models

	python_pages = [
		{"title": "Official Python Turorial",
		 "url":"http://docs.python.org/2/tutorial",
		 "views": str(random.randint(1, 101))},
		 {"title": "How to think like a computer scientist",
		 "url":"http://www.greenteapress.com/thinkpython",
		 "views": str(random.randint(1, 101))},
		 {"title": "Learn python in 10 mins",
		 "url":"http://www.korokithakis.net/tutorials/python/",
		 "views": str(random.randint(1, 101))}]

	django_pages = [
		{"title": "Official Django Tutorial",
		 "url" : "https://docs.djangoproject.com/en/1.9/intro/tutorial101/",
		 "views": str(random.randint(1, 101))},
		{"title":"Django Rocks",
		 "url":"http://www.djangorocks.com/",
		 "views": str(random.randint(1, 101))},
		{"title":"How to Tango with Django",
		 "url":"http://www.tangowithdjango.com/",
		 "views": str(random.randint(1, 101))} ]

	other_pages = [
		{"title":"Bottle",
		"url":"http://bottlepy.org/docs/dev/",
		"views": str(random.randint(1, 101))},
		{"title":"Flask",
		"url":"http://flask.pocoo.org",
		"views": str(random.randint(1, 101))} ]

	cats = {"Python": {"pages": python_pages, "views": "128","likes": "64"},
		 "Django": {"pages": django_pages,"views": "64", "likes": "32"},
		 "Other Frameworks": {"pages": other_pages, "views": "32", "likes": "16"} }

		#the code below goes through the cats (catagories) dictionary,
		#then adds each catagory

	for cat, cat_data in cats.items():
		c = add_cat(cat, cat_data["views"], cat_data["likes"])
		for p in cat_data["pages"]:
			add_page(c, p["title"], p["url"], p['views'])

		#print out the catagories we have added

	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url=url
	p.views=views
	p.save()
	return p

def add_cat(name, views, likes):
	c = Category.objects.get_or_create(name=name)[0]
	c.views=views
	c.likes=likes
	c.save()
	return c

if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()
