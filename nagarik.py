import newspaper
import pandas

nagarik_news = newspaper.build('https://myrepublica.nagariknetwork.com/category/politics', memoize_articles=False)
nagarik_news_data = []

for article in nagarik_news.articles:
    article_data = {}
    article.download()
    article.parse()
    article.nlp()
    article_data["title"] = article.title
    article_data["url"] = article.url
    article_data["summary"] = article.summary
    article_data["meta_keywords"] = article.meta_keywords
    article_data["date"] = article.publish_date
    nagarik_news_data.append(article_data)

nagarik_data = pandas.DataFrame(nagarik_news_data)
nagarik_data.to_csv('nagarik.csv')