import urllib
import BeautifulSoup

s = "http://m.apk.tw"
s1 = "http://m.apk.tw/top"

# soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(s))
soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(s1))
# print soup.title.string
# print soup.a
# print soup.div['class']
print soup.findAll("div", {"class": "content"})
