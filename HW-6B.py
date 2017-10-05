import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input("Enter url")
count = int(input("Enter count:"))
pos = int(input("Enter position:"))

def getPosName(url, pos):
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	x = [link.get('href') for link in soup.find_all('a')][pos-1]
	return x

times_left = count
while times_left != 0:
	url = getPosName(url,pos)
	times_left -= 1

final_html = urllib.request.urlopen(url).read()
final_soup = BeautifulSoup(final_html, 'html.parser')
print (final_soup.title.string.split(" ")[2])