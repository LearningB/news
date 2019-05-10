import news_extractor


nagarik = news_extractor.extractor('https://myrepublica.nagariknetwork.com/category/politics', 'myrepublica')
nagarik.save_data()

