from newsapiwrapper import news
import json # to read the api key from config

# https://newsapi.org/#documentation

# import the api key from the config
with open('config.json', 'r') as f:
	config = json.load(f)

main = news.News(config['api-key']) # start the news object w the key
search = main.sourceQuery('The-New-York-Times') # make the request 
print(search.getSource()) # print source for the request
for art in search.getArticles():
	print('\t{}\t\t{}'.format(art.getTitle(), art.getAuthor())) # print each article title in the request

# TODO: fill out docstrings