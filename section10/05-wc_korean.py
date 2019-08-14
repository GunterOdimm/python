# -*-coding: utf-8 -*-

from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Okt


text = ''
with open("res/대한민국헌법.txt",encoding="utf-8") as f:
	text = f.read();

nlp = Okt()

nouns = nlp.nouns(text)
print(nouns)

words = []
for n in nouns:
	if len(n) > 1:
		words.append(n)

print(words)

count = Counter(words)

most = count.most_common(100)
print(most)

tags = {}

for t in most:
	n,c = t

	tags[n] = c

print(tags)

wc = WordCloud(font_path="NanumGothic", width=1200, height=800, scale=2.0, max_font_size=250)

wc.generate_from_frequencies(tags)

wc.to_file("대한민국헌법-주요단어.png")

