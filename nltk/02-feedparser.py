import feedparser


llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
print(llog)
