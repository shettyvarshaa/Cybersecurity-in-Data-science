from textblob import TextBlob
from newspaper import Article
import re 

url = 'https://en.wikipedia.org/wiki/Mathematics'
article = Article(url)

article.download()
article.parse()
article.nlp()

text_clean = re.sub(r'\[\d+\]', '', text)
text = article.summary
print(text)