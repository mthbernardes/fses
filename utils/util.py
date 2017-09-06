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
	result = duckDuckGo().search(query,verbose=verbose)
	if result:
		results.extend(result)

	print "Yahoo Search"
	result = yahoo().search(query,verbose=verbose)
	if result:
		results.extend(result)

	print "Bing Search"
	result = bing().search(query,verbose=verbose)
	if result:
		results.extend(result)

	print "UOL Search"
	result = uol().search(query,verbose=verbose)
	if result:
		results.extend(result)

	print "Ask Search"
	result = ask().search(query,verbose=verbose)
	if result:
		results.extend(result)

	return results
