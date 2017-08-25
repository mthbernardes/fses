import sys
import requests
from lxml import html
from utils import util

class className():
	headers = util.getHeaders()
	results = list()
	finalResults = list()
	counter = 1

	def search(self,query,verbose=False):
		self.verbose = verbose
		url = "http://url.goes.here/search?p=%s" % query
		r = requests.get(url,headers=self.headers)
		self.searchParser(r.content)
		if self.finalResults:
			return self.finalResults

	def searchParser(self,content):
		tree = html.fromstring(content)
		urls = tree.xpath('') # You can get it using the google chrome developer tool
		nextPage = tree.xpath('') # You can get it using the google chrome developer tool
		if self.verbose: print 'Search Engine Name - Searching page %d' % self.counter
		self.counter = self.counter + 1

		for url in urls:
			self.results.append(url)
	
		if nextPage:	#or any logic you need
			self.checkNextPage(nextPage) #Pass the new link or data to call search again
		else:
			self.finalResults = self.results # Return the urls

	def checkNextPage(self,nextPage):
		#You code goes here
		self.search(query,verbose=self.verbose)

