import newspaper
import pandas
from urllib.parse import urlparse

kantipur_news = newspaper.build('https://www.kantipurdaily.com/business',memoize_articles=False, language='hi')
kantipur_news_data = []

for article in kantipur_news.articles:
    article_data = {}
    if "kantipurdaily" in article.url:
        try:
            article.download()
            article.parse()
            article.nlp()
            article_data["title"] = article.title
            article_data["url"] = article.url
            article_data["category"] = urlparse(article.url).path.split('/')[1]
            article_data["summary"] = article.summary
            article_data["meta_keywords"] = article.meta_keywords
            article_data["date"] = article.publish_date
            kantipur_news_data.append(article_data)
        except:
            continue



kantipur_data = pandas.DataFrame(kantipur_news_data)
kantipur_data.to_csv("kantipur_news_nepali.csv")

