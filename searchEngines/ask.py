import sys
import requests
from lxml import html
from utils import util

class ask():
	headers = util.getHeaders()
	results = list()
	finalResults = list()
	counter = 1

	def search(self,query,pageId=1,verbose=False):
		self.verbose = verbose
		url = "https://www.search.ask.com/web?q=%s&o=&tpr=10&page=%d" % (query,pageId)
		r = requests.get(url,headers=self.headers)
		self.searchParser(r.content)
		if self.finalResults:
			return self.finalResults

	def searchParser(self,content):
		tree = html.fromstring(content)
		urls = tree.xpath('//*[@id="algo-container"]/ol/li/div/a/@href')
		nextPage = tree.xpath('//*[@id="pagination-nav-block"]/div/a[2]/@href')
		if self.verbose: print 'Ask - Searching page %d' % self.counter
		self.counter = self.counter + 1
		for url in urls:
			self.results.append(url)
		if len(nextPage) != 0:
			if len(nextPage) == 2 or self.counter - 1 == 1:
				self.checkNextPage(nextPage)
			else:
				self.finalResults = self.results
		else:
			self.finalResults = self.results

	def checkNextPage(self,nextPage):
		query,pageId = nextPage[-1].split("&")[2].split("=")[1],nextPage[-1].split("&")[3].split("=")[1]
		self.search(query,int(pageId),verbose=self.verbose)

