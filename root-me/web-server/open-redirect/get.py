#http://challenge01.root-me.org/web-serveur/ch52/?url=https://google.com&h=99999ebcfdb78df077ad2727fd00969f

import httplib, urllib

params = urllib.urlencode({'url': 'https://google.com', 'h': '99999ebcfdb78df077ad2727fd00969f'})
headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}
conn = httplib.HTTPConnection("challenge01.root-me.org/web-serveur/ch52/")
conn.request("GET", "/", params, headers)
response = conn.getresponse()
#print response.status, response.reason

data = response.read()
print data

conn.close()