#coding=utf-8
from goose import Goose
url = 'https://www.ucl.ac.uk/legal-services/privacy'
g = Goose()

article = g.extract(url=url)
print article.title.encode('utf-8')
print article.cleaned_text.encode('utf-8')

