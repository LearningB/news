import newspaper
import pandas

ratopati_news = newspaper.build('http://english.ratopati.com', memoize_articles=False)
ratopati_data = []

for article in ratopati_news.articles:
    articles_data = {}
    article.download()
    article.parse()
    article.nlp()
    articles_data["title"] = article.title
    articles_data["url"] = article.url
    # articles_data["category"] = urlparse(article.url).path.split('/')[1]
    articles_data["summary"]= article.summary
    articles_data["meta-keywords"] = article.meta_keywords
    ratopati_data.append(articles_data)

ratopati_database = pandas.DataFrame(ratopati_data)
ratopati_database.to_csv("ratopati.csv")