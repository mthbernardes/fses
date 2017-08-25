import requests
from pprint import pprint
from lxml import html
from utils import util


class uol():
	headers = util.getHeaders()
	results = list()
	finalResults = list()
	counter = 1

	def search(self,query,pageId=1,verbose=False):
		self.verbose = verbose
		self.query = query
		self.headers['Referer']='https://busca.uol.com.br/result.html?term=%s' % query
		url = "https://busca.uol.com.br/search?client=uol&term=%s&page=%d" % (query,pageId)
		r = requests.get(url,headers=self.headers)
		self.searchParser(r.json())
		if self.finalResults:
			return self.finalResults

	def searchParser(self,content):
		if content['results']:
			if self.verbose: print 'UOL - Searching page %d' % self.counter
			for response in content['results']:
				self.results.append(response['url'])
			self.counter = self.counter + 1
			self.search(self.query,self.counter,verbose=self.verbose)
		else:
			self.finalResults = self.results

