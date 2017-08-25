import requests
from lxml import html
from utils import util

class bing():

	headers = util.getHeaders()
	results = list()
	finalResults = list()
	counter = 1

	def search(self,query,verbose = False):
		self.verbose = verbose
		url = 'https://www.bing.com/search?q=%s' % query
		r = requests.get(url,headers=self.headers)
		self.searchParser(r.content)
		if self.finalResults:
			return self.finalResults

	def searchParser(self,content):
		tree = html.fromstring(content)
		urls = tree.xpath('//*[@id="b_results"]/li/h2/a/@href')
		nextPage = tree.xpath('//*[@id="b_results"]/li[11]/nav/ul/li[6]/a/@href')
		if self.verbose: print 'Bing - Searching page %d' % self.counter
		self.counter = self.counter + 1

		for url in urls:
			self.results.append(url)

		if nextPage:
			self.checkNextPage(nextPage)
		else:
			self.finalResults = self.results

	def checkNextPage(self,nextPage):
		query = nextPage[0].split("=",1)[1]
		self.search(query,verbose=self.verbose)