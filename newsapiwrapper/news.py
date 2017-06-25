#!/usr/bin/env python

# info: https://www.alphavantage.co/documentation/
# i.e. https://www.alphavantage.co/query?function=global_quote&symbol=appl&apikey={{key}}

import requests as r

class News(object):
	key = None
	"""docstring for AVConnect"""
	def __init__(self, key):
		self.key = key

	def sourceQuery(self, query):
		return SourceQuery(self.key, query)

class SourceQuery(object):
	"""docstring for SourceQuery"""
	key = None
	raw = None
	source = None
	articlesMade = False

	status = None
	source = None
	sortBy = None

	articles = []

	def __init__(self, apikey, source):
		self.key = apikey
		self.source = source
		self.raw = self.get()

	def get(self):
		"""docstring..."""
		path = 'https://newsapi.org/v1/articles?source={}&apikey={}'.format(self.source, self.key)
		with r.Session() as s:
			self.raw = s.get(path).json()
			return(self.raw)

	def getStatus(self):
		"""docstring..."""
		self.status = self.raw['status']
		return self.status

	def getSource(self):
		"""docstring..."""
		self.source = self.raw['source']
		return self.source
		
	def getSortBy(self):
		"""docstring..."""
		self.top = self.raw['sortBy']
		return self.top

	def getArticles(self):
		"""..."""
		if not self.articlesMade:
			for a in self.raw['articles']:
				a = Article(a)
				self.articles.append(a)
		return self.articles

class Article(object):
	"""docstring for Article"""
	raw = None

	author = None
	title = None
	description = None
	url = None
	imageUrl = None
	publishedAt = None

	def __init__(self, value):
		self.raw = value
		# print(value)
		
	def getAuthor(self):
		"""TODO: make docstring"""
		self.author = self.raw['author']
		return self.author

	def getTitle(self):
		"""TODO: make docstring"""
		self.title = self.raw['title']
		return self.title

	def getDescription(self):
		"""TODO: make docstring"""
		self.description = self.raw['description']
		return self.description

	def getUrl(self):
		"""TODO: make docstring"""
		self.url = self.raw['url']
		return self.url

	def getImageUrl(self):
		"""TODO: make docstring"""
		self.imageUrl = self.raw['imageUrl']
		return self.imageUrl

	def getPublishedAt(self):
		"""TODO: make docstring"""
		self.publishedAt = self.raw['publishedAt']
		return self.publishedAt
