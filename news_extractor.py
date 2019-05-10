import newspaper
import pandas
from urllib.parse import urlparse

class extractor:
    # language in the next iteration
    def __init__(self,url,paper):
        self.url = url
        self.paper = paper


    def save_data(self):
        newspaper_database = []
        
        newspaper_build = newspaper.build(self.url, memoize_articles=False)

        for article in newspaper_build.articles:
            newspaper_info = {}
            if self.paper in article.url:
                try:
                    article.download()
                    article.parse()
                    article.nlp()
                    print(article.url)
                    newspaper_info["url"] = article.url
                    newspaper_info["title"] = article.title
                    newspaper_info["summary"] = article.summary
                    newspaper_info["meta_keywords"] = article.meta_keywords
                    newspaper_info["date"] = article.publish_date
                    newspaper_database.append(newspaper_info)
                except:
                    continue

        newspaper_info = pandas.DataFrame(newspaper_database)
        newspaper_info.to_csv(newspaper_build.brand +'.csv')