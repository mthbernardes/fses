import requests
from lxml import html
from utils import util
from urllib import unquote


class yahoo():
	headers = util.getHeaders()
	results = list()
	finalResults = list()
	counter = 1

	def search(self,query=None,url=None,verbose=False):
		self.verbose = verbose
		url = url if url else 'https://br.search.yahoo.com/search?&p=%s' % query
		r = requests.get(url,headers=self.headers)
		self.searchParser(r.content)
		if self.finalResults:
			return self.finalResults

	def searchParser(self,content):
		tree = html.fromstring(content)
		urls = tree.xpath('//*[@class=" td-u"]/@href')
		nextPage = tree.xpath('//*[@class="next"]/@href')
		if self.verbose: print 'Yahoo - Searching page %d' % self.counter
		self.counter = self.counter + 1

		for url in urls:
			self.results.append(unquote(url).split("RU=")[1].split("/RK=")[0])
			
		if nextPage:
			self.checkNextPage(nextPage)
		else:
			self.finalResults = self.results

	def checkNextPage(self,nextPage):
		self.search(url=nextPage[0],verbose=self.verbose)

