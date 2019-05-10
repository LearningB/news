import newspaper
import pandas
from urllib.parse import urlparse

annapurna_times = newspaper.build('https://theannapurnaexpress.com/', memoize_articles=False)
annapurna_times_data = []

for article in annapurna_times.articles:
    try:
        articles_data = {}
        article.download()
        article.parse()
        article.nlp()
        articles_data["title"] = article.title
        articles_data["url"] = article.url
        # articles_data["category"] = urlparse(article.url).path.split('/')[1]
        articles_data["summary"]= article.summary
        articles_data["meta-keywords"] = article.meta_data.get('keywords')
        annapurna_times_data.append(articles_data)
    except:
        continue

annapurna_data = pandas.DataFrame(annapurna_times_data)
annapurna_data.to_csv("annapurna.csv")