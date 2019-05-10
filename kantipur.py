import newspaper
import pandas

kantipur_news = newspaper.build("http://kathmandupost.ekantipur.com/", memoize_articles=False)
kantipur_news_data = []

for article in kantipur_news.articles:
    article_data = {}
    if "kathmandupost" in article.url:
        article.download()
        article.parse()
        article.nlp()
        article_data["title"] = article.title
        article_data["url"] = article.url
        article_data["category"] = article.meta_keywords[-3]
        article_data["summary"] = article.summary
        article_data["meta_keywords"] = article.meta_keywords
        article_data["date"] = article.publish_date
        kantipur_news_data.append(article_data)



kantipur_data = pandas.DataFrame(kantipur_news_data)
kantipur_data.to_csv("kantipur_news.csv")

