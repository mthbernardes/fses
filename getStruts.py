from utils import util
from urlparse import urlparse

'''
usage example
Get .actions pages to exploit using CVE-2017-9805
'''

query = "filetype:action"
results = set(util.searchAll(query,verbose=False))
print 'Total domains found: %d' % len(results)
for result in results:
	print "[+] - %s" % result

