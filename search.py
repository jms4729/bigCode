import httplib

conn = httplib.HTTPSConnection("api.github.com")

#all of c projects in github
conn.putrequest("GET", "/search/repositories?q=+language:c&sort=stars&order=desc")
#all of c projects containing word Makefile in README
#conn.putrequest("GET", "/search/repositories?q=Makefile+language:c&sort=stars&order=desc")
	
	
conn.putheader("User-Agent", "MyTest")
conn.endheaders()

res = conn.getresponse()

print res.status, res.reason
print res.read()
