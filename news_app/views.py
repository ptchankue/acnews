from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
#from django.contrib.gis.geoip import GeoIP

# Create your views here.
from extractor import Extractor
from news_app.models import Article, Visitor

import HTMLParser
html_parser = HTMLParser.HTMLParser()
#unescaped = html_parser.unescape(my_string)

#bot = Extractor()
#bot.parseRadiOkapi()

def test(request):

	return HttpResponse('This is a test...<img src=/statics/images/social.png></img>')


def index (request):

	articles = Article.objects.all().order_by('-fetched_on')

	ip = request.META['REMOTE_ADDR']
	print 'In index...\n', ip

	visitor = Visitor.objects.filter(ip = ip)
	if visitor.count() == 0:
		# New comer
		visitor 		= Visitor()
		visitor.ip 		= request.META['REMOTE_ADDR']
		visitor.save()
		print visitor.__dict__
	else:
		# Not a new comer
		visitor 		= visitor.first()
		visitor.nb_visit +=1
		visitor.last_visit = timezone.now()
		visitor.save()
		print visitor.__dict__

	context = {}

	context['author'] 		= 'Dr Patrick Tchankue'

	context['articles']		= articles

	return render_to_response('index.html', context)

def contact(request):
	return render_to_response('contact.html')

def category(request):
	return render_to_response('contact.html')
