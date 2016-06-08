import urllib
import BeautifulSoup

s = "http://m.apk.tw"
s1 = "http://m.apk.tw/top"

# soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(s))
soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(s1))
# print soup.title.string
# print soup.a
# print soup.div['class']
# print soup.findAll("div", {"class": "content"})[0]

# for clas in soup.findAll("div", {"class": "content"}):
#     for h3 in clas.findAll("h3"):
#         print(h3.contents.get('href'))
#

# for clas in soup.findAll("div", {"class": "content"}):
#     for a in clas.findAll("a"):
#         if a.get('class') == "down":
#             print(a.get('href'))


content = soup.findAll("div", {"class": "content"})[0]
for tag_a in content.findAll("a"):
    if tag_a.get('class') == "down":
        print(tag_a.get('href'))
