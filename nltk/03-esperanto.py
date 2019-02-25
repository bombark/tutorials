import nltk

#nltk.download('punkt')
f = open("eo-articles.txt", "r")
raw_text = f.read().decode("utf-8").lower()

tokens = nltk.word_tokenize(raw_text,language='portuguese')
#tokens = set(tokens)

#print(tokens)

substantivaro = set()
verbaro = set()

adjektivaro = set()

fd = nltk.FreqDist(tokens)
for key in sorted(fd, key=fd.get, reverse=False):
	if len(key) > 3:
		if key[-1] == 'o':
			substantivaro.add(key)
			substantivaro.add(key+"n")
			substantivaro.add(key+"j")
			substantivaro.add(key+"jn")

		elif key[-1]=='j' and key[-2]=='o':
			substantivaro.add(key[0:-1])
			substantivaro.add(key[0:-1]+"n")
			substantivaro.add(key)
			substantivaro.add(key+"n")

		elif key[-1]=='n' and key[-2]=='o':
			substantivaro.add(key[0:-1])
			substantivaro.add(key)
			substantivaro.add(key[0:-1]+"j")
			substantivaro.add(key[0:-1]+"jn")

		elif key[-1]=='n' and key[-2]=='j' and key[-3]=='o':
			substantivaro.add(key[0:-2])
			substantivaro.add(key[0:-2]+"n")
			substantivaro.add(key[0:-1])
			substantivaro.add(key)

		if key[-1] == 'a' or ( key[-1] == 'j' and key[-2] == 'a' ) or \
			( key[-1] == 'n' and key[-2] == 'a' ) or \
			( key[-1] == 'n' and key[-2] == 'j' and key[-3] == 'a' ):
			adjektivaro.add(key)



		# if key[-1] == 's' and key[-2] == 'u':
		# 	print(key[0:-2]+"i")

		if  key[-1] == 's' and key[-2] == 'a' or \
			key[-1] == 's' and key[-2] == 'o' or \
			key[-1] == 's' and key[-2] == 'i':
			verbaro.add(key[0:-2]+"i")

		if key[-1] == 'i':
			verbaro.add(key)



# for vorto in sorted(verbaro):
# 	print "- {name: "+format(vorto)+", class: vi}"
# 	print "- {name: "+format(vorto[0:-1]+"is")+", class: vc, time: past}"
# 	print "- {name: "+format(vorto[0:-1]+"as")+", class: vc, time: present}"
# 	print "- {name: "+format(vorto[0:-1]+"os")+", class: vc, time: future}"
# 	print "- {name: "+format(vorto[0:-1]+"us")+", class: vc, time: conditional}"


# for vorto in sorted(substantivaro):
# 	print "- {name: "+format(vorto).encode("utf-8")+", class: noun}"


for vorto in sorted(adjektivaro):
	print "- {name: "+format(vorto).encode("utf-8")+", class: adj}"
