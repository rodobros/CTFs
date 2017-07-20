import md5 #Must be run in python 2.7.x

#code used to calculate successive hashes in a hashchain. 
seed = "8939"

#this will find the 5th hash in the hashchain. This would be the correct response if prompted with the 6th hash in the hashchain
hashc = seed
for _ in xrange(1000):
	if hashc == "2b4968515eacc4c2e0f62aae28db08c2":
		break;
	hashc = md5.new(hashc).hexdigest()
	print hashc

 
