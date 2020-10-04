class Source(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.articles = []

    def addArticle(heading, url):
        self.articles.append((heading, url))