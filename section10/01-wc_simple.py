#-*-coding: utf-8 -*-

from wordcloud import WordCloud

text =''
with open("res/이상한나라의앨리스.txt", encoding="utf-8") as f:
	text = f.read()

print(text)

wc = WordCloud(width=1200, height=800)

wc.generate(text)

print(wc.words_)

wc.to_file("simple.png")