from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.


def test(request):
	return HttpResponse('This is a test...<img src=/statics/images/social.png></img>')

	
def index (request):
	print 'In index...'
	return render_to_response('index.html')

def contact(request):
	return render_to_response('contact.html')