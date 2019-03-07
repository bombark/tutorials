import feedparser
import yaml
import nltk
from nltk.corpus import wordnet





#http://feeds.bbci.co.uk/news/world/rss.xml
# llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
# words = []
# newspkg = feedparser.parse("http://rss.dw.com/atom/rss-en-all")
# for news in newspkg["entries"]:
# 	#print(news["title"])     # ,news['links'][0]['href'])
# 	#print(news["summary"])
# 	text = news["title"] + news["summary"]
# 	tokens = nltk.word_tokenize(text.lower(),language='english')
# 	words += tokens
#
# newspkg = feedparser.parse("http://feeds.bbci.co.uk/news/world/rss.xml")
# for news in newspkg["entries"]:
# 	#print(news["title"])     # ,news['links'][0]['href'])
# 	#print(news["summary"])
# 	text = news["title"] + news["summary"]
# 	tokens = nltk.word_tokenize(text,language='english')
# 	words += tokens
#
# for word in sorted(set(words)):
# 	print( word )

#tagged = nltk.pos_tag( sorted(set(words)) )
# print("data:")
# for item in tagged:
# 	print("  - {name: "+item[0]+", tag: "+item[1]+" }")

import os

fd = open("vortaro-en.txt")
data = yaml.load(fd.read())
for item in data["data"]:
	if item['tag'] == 'NN' or item['tag'] == 'NNS':
		cmd = "googleimagesdownload -k "+item['name']+" -l 3"
		os.system(cmd)
		#print(item)
