import newspaper
import pandas

nepali_times_news = newspaper.build("https://www.nepalitimes.com/", memoize_articles=False)
nepali_times_news_data = []


for article in nepali_times_news.articles:
    article_data = {}
    article.download()
    article.parse()
    article.nlp()
    article_data["title"] = article.title
    article_data["url"] = article.url
    print(article.meta_data)
    # article_data["category"] = article.meta_keywords[-3]
    article_data["summary"] = article.summary
    article_data["meta_keywords"] = article.meta_keywords
    article_data["date"] = article.publish_date
    nepali_times_news_data.append(article_data)



nepali_times_data = pandas.DataFrame(nepali_times_news_data)
nepali_times_data.to_csv("nepali_times_news.csv")

