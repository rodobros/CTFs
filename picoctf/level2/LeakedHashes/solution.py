import md5

hashdump = open("./hashdump.txt", "r").readlines()
hash_list = []
hash_dic = {}
for h in hashdump:
	name = h.split(":")[0]
	hashvalue = h.split(":")[1].strip() # strip to remove \n
	hash_dic[hashvalue] = name
	hash_list.append(hashvalue)
#hash_list = map(lambda x : x.split(":")[1], hash_list)

words = open("./common_passwords.txt", "r")
word_list = words.readlines()
word_list = map(lambda x : x.strip(), word_list)

for w in word_list:
	hashvalue = md5.new(w).hexdigest()
	if hashvalue in hash_list:
		answer = "name: " + hash_dic[hashvalue] + ", password: " + w
		print answer


