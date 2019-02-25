import yaml
import cherrypy
import nltk
import json


class Word:
	def __init__(self,raw):
		self.klass = raw["class"]
		self.name  = raw["name"]

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

	def __str__(self):
		return self.toJSON()

class Noun(Word):
	pass
	# def __init__(self,raw={}):
	# 	Word.__init__(self,raw)
	# 	self.klass = "noun"

class Adjective(Word):
	pass
	# def __init__(self,raw={}):
	# 	Word.__init__(self,raw)
	# 	self.klass = "adj"


class Vortaro:
	def __init__(self):
		self.vortoj = {}

	def get(self,word):
		return self.vortoj[word]

	def includeFile(self,filename):
		f = open(filename, "r")
		list = yaml.load(f)
		for word in list["data"]:
			name = word["name"]
			klass = word["class"]
			novo = Word(word)

			if name in self.vortoj:
				self.vortoj[ name ].append( novo )
			else:
				list = []
				list.append(novo)
				self.vortoj[ name ] = list



class Server(object):
	@cherrypy.expose
	def index(self,raw):
		tokens = nltk.word_tokenize(raw,language='portuguese')
		res = []
		for word in tokens:
			list = self.vortaro.get(word)

			#subres = []
			#for item in list:
			#	subres.append( str(item) )

			res.append( list )
		return json.dumps(res)


	def boot(self):
		self.vortaro = Vortaro()
		self.vortaro.includeFile("adjetivaro.yml")
		#self.vortaro.includeFile("substativaro.yml")



server = Server()
server.boot()
cherrypy.quickstart(server)


# vortaro = Vortaro()
# vortaro.includeFile("adjetivaro.yml")
# vortaro.includeFile("substativaro.yml")
#
# print("loaded")
# while True:
# 	word = input("")
# 	list = vortaro.get( word )
# 	for word in list:
# 		print(word)
