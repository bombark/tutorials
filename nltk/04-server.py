import yaml
import cherrypy
import nltk
import json
import vortaro


class Server(object):
	@cherrypy.expose
	def index(self,raw=""):
		tokens = nltk.word_tokenize(raw,language='portuguese')
		res = { 'tokens': tokens, 'dictionary': {} }

		for word in tokens:
			tag_list = []
			list = self.vortaro.get(word)
			for tag in list:
				tag_mapped = {'name': tag.name, 'class': tag.klass}
				tag_list.append(tag_mapped)
			if len(tag_list) == 0:
				res['dictionary'][word] = {'class': 'null'}
			elif len(tag_list) == 1:
				res['dictionary'][word] = tag_list[0]
			else:
				res['dictionary'][word] = tag_list
		return json.dumps(res)

	@cherrypy.expose
	def data(self,raw=""):
		return json.dumps({ 'class': 'map', 'data': raw })

	def boot(self):
		self.vortaro = vortaro.Dictionary()
		self.vortaro.includeFile("vortaro-en.yml")
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
