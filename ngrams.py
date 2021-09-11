"""
Source:
 - https://towardsdatascience.com/web-scraping-using-python-4cb2faade338
 - https://albertauyeung.github.io/2018/06/03/generating-ngrams.html
"""

import re
from collections import Counter
from bs4 import BeautifulSoup
from nltk.util import ngrams
from urllib.request import urlopen

# specify the url
url = "https://karpathy.github.io/2019/04/25/recipe/"

# Connect to the website and return the html to the variable ‘page’
try:
    page = urlopen(url)
except:
    print("Error opening the URL")

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
content = soup.find('article', {"class": "post-content"})

article = ''
for i in content.findAll('p'):  # what about headers?
    article = article + ' ' +  i.text
print(article)

s = article.lower()
s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
tokens = [token for token in s.split(" ") if token != ""]
output = list(ngrams(tokens, 5))

most_common = Counter(output).most_common(10)
print(most_common)

# Most common are garbagge. The good is somewhat rare. Like: "leaky abstraction", "neural net training", "success in deep learning". How to get them?
