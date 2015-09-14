#!/usr/bin/python


from bs4 import BeautifulSoup
import urllib2, os
from datetime import datetime

os.environ["DJANGO_SETTINGS_MODULE"] = "acnews.settings"

from news_app.models import Article

def parse(article):
	print article.find('a', {'class':'modal'})


url= 'http://rfi.fr/afrique'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(),  'html.parser')

sections = soup.findAll('section', {'id':'news'})

#anchors = [td.find('a') for td in soup.findAll('li', {'data-bo-type':'article'})]
articles = soup.findAll('li', {'data-bo-type':'article'})
print 'Number of article:', len(articles)
for article in articles[:5]:
	if article:
		a = article.find('a')
		if a.get('title'):
			post = Article()
			print a.get('title').encode('cp850', errors='replace').decode('cp850')
			post.title =  a.get('title').encode('cp850', errors='replace').decode('cp850')

			print 'Link:', a['href']
			post.link = 'http://rfi.fr' + a['href']

			print a.get('data-height')
			if a.get('data-image'):
				print 'Image:', a.get('data-image')
				post.thumbnail =  a.get('data-image')

			posts = Article.objects.filter(link = post.link)
			if posts.count()==0:
				post.source = 'RFI Afrique'
				post.view_count = 0
				post.fetched_on = datetime.now()
				print post.__dict__
				post.save()


			print '---'*20

			print '\n\nFrom my database:'
posts = Article.objects.all()
for post in posts:
	print post.link, post.title
print '\n\nArticle #', posts.count()
