import requests
from lxml import html
from utils import util

class duckDuckGo():
	headers = util.getHeaders()
	results = list()
	finalResults = list()
	counter = 1

	def search(self,query,data=None,verbose=False):
		self.verbose = verbose
		self.query = query
		request = requests.post if data else requests.get
		url = "https://duckduckgo.com/html/?q=%s&s=0" % (query)
		r = request(url,headers=self.headers,data=data)
		self.searchParser(r.content)
		if self.finalResults:
			return self.finalResults

	def searchParser(self,content):
		tree = html.fromstring(content)
		urls = tree.xpath('//*[@id="links"]/div/div/h2/a/@href')
		nextPage = tree.xpath('//div[@class="nav-link"]/form')
		if self.verbose: print 'Duck Duck Go - Searching page %d' % self.counter
		self.counter = self.counter + 1
		for url in urls:
			self.results.append(url)

		self.checkNextPage(nextPage)

	def checkNextPage(self,nextPage):
		if nextPage:
			dataNetxPage = dict()
			for form in nextPage:
				for field in form.getchildren():
					dataNetxPage[field.get('name')]=field.get('value')
			self.search(self.query,data=dataNetxPage,verbose=self.verbose)
		else:
			self.finalResults = self.results

if __name__ == '__main__':
	print "You shall not pass!"