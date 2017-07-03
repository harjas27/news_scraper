import requests
from bs4 import BeautifulSoup
import os

def get_news():
	kinds=['india','world','sports','cities']
	url='http://indianexpress.com/section/'
	os.mkdir('news')
	for kind in kinds :
		fol='news'
		url=url+kind+'/'
		page = requests.get(url,verify=False)

		#print(page.content)

		soup = BeautifulSoup(page.content, 'html.parser')

		p = soup.find('body')
		os.mkdir(fol+'/'+kind)
		'''target = open('country/body.txt', 'w')
		target.write(str(p))'''

		ars = p.find_all(class_='articles')
		fname=''
		fname+=fol+'/'+kind+'/articles.txt'
		target = open(fname,'w')
		articles={}

		for a in ars :
			ttl = a.find(class_='title')
			articles[ttl.get_text()]=ttl.find('a').get('href')

		for a in articles :
			target.write("".join([x if ord(x) < 128 else '' for x in a]))
			target.write('\n')
			target.write(str(articles[a]))
			target.write("\n**************************************************************\n")	