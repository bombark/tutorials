import nltk

print("opa")

#nltk.download('brown')
#https://raw.githubusercontent.com/nltk/nltk_data/ghpages/packages/corpora/brown.zip
# nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
# nltk.download('machado')
# nltk.download('floresta')

#sentence = """   ele    esta    (no caminhao amarelo)."""
#tokens = nltk.word_tokenize(sentence,language='portuguese')
#print(tokens)
#tagged = nltk.pos_tag(tokens)
#print(tagged)



#from nltk.corpus import machado
#sent_tokenizer=nltk.data.load('tokenizers/punkt/portuguese.pickle')
#raw_text = machado.raw('romance/marm05.txt')
#sentences = sent_tokenizer.tokenize(raw_text)
#for sent in sentences[0:15]:
#	print(sent)


#from nltk.corpus import machado

#raw_text = machado.raw('romance/marm05.txt')
#tokens = nltk.word_tokenize(raw_text,language='portuguese')
#fd = nltk.FreqDist(tokens)
#lista = sorted( set(tokens) )
#for key in sorted(fd, key=fd.get, reverse=False):
#	print key, fd[key]



# nltk.download('stopwords')


# from nltk.corpus import machado
#
# raw_text = machado.raw('romance/marm05.txt')
# tokens = nltk.word_tokenize(raw_text,language='portuguese')
# tokens = set(tokens)
#
# tagged = nltk.pos_tag(tokens)
# print(tagged)
