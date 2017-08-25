# fses

Fucking Search Engines Scraper - python library to scrap url's from search engines

# Search Engines we scrap
<pre>
Ask
Bing
DuckDuck GO
UOL
Yahoo
</pre>

# Install
<pre>
git clone https://github.com/mthbernardes/fses.git
cd fses
pip install -r requeriments.txt
</pre>

# Usage

<b>Simple search using Ask</b>
<pre>
from searchEngines.ask import ask

print "Ask Search"
query = "site:domain.com" # Set a dork
a = ask() # Start a instance of any search engine
results = a.search(query,verbose=True) #All classes use the method search, verbose is used just to print, what page the script is scraping
for url in results
	print url
</pre>

<b>All search engine methods</b>
<pre>
query = "site:domain.com"

from searchEngines.ask import ask
print "Ask Search"
results.extend(ask().search(query,verbose=verbose))

from searchEngines.uol import uol
print "UOL Search"
results.extend(uol().search(query,verbose=verbose))

from searchEngines.bing import bing
print "Bing Search"
results.extend(bing().search(query,verbose=verbose))

from searchEngines.yahoo import yahoo
print "Yahoo Search"
results.extend(yahoo().search(query,verbose=verbose))	

from searchEngines.duckduckgo import duckDuckGo
print "DuckDuckGo Search"
results.extend(duckDuckGo().search(query,verbose=verbose))
</pre>

<b>Search using all search engines</b>
<pre>
from utils import util
query = "site:conviso.com.br"
results = util.searchAll(query,verbose=False) #searchAll has the same properties then search method
for url in results
	print url
</pre>

# How to create a search engine plugin

Just follow the searchEngines/example.py, it's a template of how to create a plugin to another search engine.

# Greatz

<a href="https://github.com/googleinurl">GoogleINURL<a>

<a href="https://github.com/jcesarstef">jcesarstef</a>



