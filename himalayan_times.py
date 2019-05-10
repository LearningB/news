import newspaper
import pandas
from urllib.parse import urlparse

himalayan_times = newspaper.build('https://thehimalayantimes.com/', memoize_articles=False)
himalayan_times_data = []

for article in himalayan_times.articles:
    articles_data = {}
    article.download()
    article.parse()
    article.nlp()
    articles_data["title"] = article.title
    articles_data["url"] = article.url
    articles_data["category"] = urlparse(article.url).path.split('/')[1]
    articles_data["summary"]= article.summary
    articles_data["meta-keywords"] = article.meta_data.get('keywords')
    himalayan_times_data.append(articles_data)

himalayan_data = pandas.DataFrame(himalayan_times_data)
himalayan_data.to_csv("himalayan.csv")