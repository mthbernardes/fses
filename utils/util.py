def getHeaders():
	import os
	import random

	filePath = os.path.join(os.getcwd(),'utils','userAgents.list')
	userAgent = random.choice(list(open(filePath))).strip()
	headers = {'User-Agent':userAgent}
	return headers

def searchAll(query,verbose=False):
	from searchEngines.ask import ask
	from searchEngines.uol import uol
	from searchEngines.bing import bing
	from searchEngines.yahoo import yahoo
	from searchEngines.duckduckgo import duckDuckGo

	results = list()

	print "DuckDuckGo Search"
	results.extend(duckDuckGo().search(query,verbose=verbose))
	
	print "Yahoo Search"
	results.extend(yahoo().search(query,verbose=verbose))
	
	print "Bing Search"
	results.extend(bing().search(query,verbose=verbose))
	
	print "UOL Search"
	results.extend(uol().search(query,verbose=verbose))
	
	print "Ask Search"
	results.extend(ask().search(query,verbose=verbose))
	
	return results
