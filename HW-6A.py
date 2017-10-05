from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
nums = [str(x) for x in range(10)]
tags = BeautifulSoup(urlopen('http://py4e-data.dr-chuck.net/comments_31867.html').read(), "html.parser")('span')
content = [x.contents for x in tags]
total = 0
for x in content:
	for num in x:
		total += int(num)
print (total)