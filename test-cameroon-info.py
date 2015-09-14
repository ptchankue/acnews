#!/usr/bin/python

from bs4 import BeautifulSoup
import urllib2, re, os
from datetime import datetime

os.environ["DJANGO_SETTINGS_MODULE"] = "acnews.settings"

from news_app.models import Article


url= 'http://cameroon-info.net'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(),  'html.parser')

articles = soup.find_all('td', {'width': '475'})
for a in articles[7:]:
	print '-'*60
	if a:
		post = Article()
		link = a.find('a', {'class': 'morehltitle2012'})
		if link :
			print 'Link ', link.get('href')
			post.link = url + link.get('href')

		desc = a.find('div', {'class': 'morehldesc'})
		if desc :
			print 'Title:\n', desc.encode('cp850', errors='replace').decode('cp850'), '\n\n', desc.get_text().encode('cp850', errors='replace').decode('cp850')
			post.title = desc.get_text().encode('cp850', errors='replace').decode('cp850')
			if desc.img:
				print '\n\nImage', url + desc.img.get('src')
				post.thumbnail = url + desc.img.get('src')
		source = a.find('div', {'class': 'morehlsource'})
		if source:
			print source.encode('cp850', errors='replace').decode('cp850')
			post.source = source.get_text().encode('cp850', errors='replace').decode('cp850')
		post.view_count = 0

		posts = Article.objects.filter(link = post.link)
		if posts.count()==0:
			post.fetched_on = datetime.now()
			post.save()

print '\n\nFrom my database:'
posts = Article.objects.all()
for post in posts:
	print post.link, post.title
print '\n\nArticle #', posts.count()
