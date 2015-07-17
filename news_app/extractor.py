
from BeautifulSoup import BeautifulSoup
import urllib2

class Extractor():

	def __init__(self, **attrs):
		print 'Constructor...'

	def parseRadiOkapi(self):
	    url = "http://www.radiookapi.net/"
	    page = urllib2.urlopen(url)
	    soup = BeautifulSoup(page.read())

	    print  'Parsing http://radiookapi.net'

	    blocks = soup.findAll('h2')

	    for a in blocks:
	        for item in a.findAll('a'):
	            print item['href']
	            #print item.get('href') + "," + item.string
	    """
	    print '*'*50
	    other = soup.findAll('div', {'class':'shashinThumbnailDiv'})
	    for a in other:
	        for item in a.findAll('a'):
	            if item.img:
	                print item.img['src']

	            print '''
	            Full item: %s\nLink:%s\nThumbnail:%s\n
	            Text:%s'''%(item, item['href'], item.img['src'], item.string)
	    """