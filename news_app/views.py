from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings
#from django.contrib.gis.geoip import GeoIP

# Create your views here.
from extractor import Extractor
from news_app.models import Article

import HTMLParser
html_parser = HTMLParser.HTMLParser()
#unescaped = html_parser.unescape(my_string)

#bot = Extractor()
#bot.parseRadiOkapi()

def test(request):

	return HttpResponse('This is a test...<img src=/statics/images/social.png></img>')


def index (request):

	articles = Article.objects.all().order_by('-fetched_on')


	print 'In index...\n', request.META['REMOTE_ADDR']
	context = {}

	context['author'] 		= 'Dr Patrick Tchankue'

	context['articles']		= articles

	return render_to_response('index.html', context)

def contact(request):
	return render_to_response('contact.html')

def category(request):
	return render_to_response('contact.html')
