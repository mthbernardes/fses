from utils import util
from urlparse import urlparse

'''
usage example
Get all subdomains of a domain, using all search engines plugins
'''

query = "site:domain.com"
results = set(util.searchAll(query,verbose=False))
domains = set()
for result in results:
	domains.add(urlparse(result).hostname)

print 'Total domains found: %d' % len(domains)
for domain in domains:
	print "[+] - %s" % domain




