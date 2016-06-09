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


# content = soup.findAll("div", {"class": "content"})[0]
# for tag_a in content.findAll("a"):
#     if tag_a.get('class') == "down":
#         print(tag_a.get('href'))

# list1 = soup.findAll("div", {"class": "w240 mt-12 mr-15"})[0]
# print list1.find("div", {"class": "title"}).h3.string
# print list1.find("div", {"class": "tab"}).span
# for a in list1.findAll("a"):
#     if a.get('class') == "down":
#         print(a.get('href'))


def _get_d_url(durl):
    # durl = "http://m.apk.tw/app/com.android.vending/"
    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(durl))
    dclass = soup.find("div", {"class": "download"})
    print " o " + dclass.find("a").get('href')

w240 = soup.findAll("div", {"class": "w240 mt-12 mr-15"})[0]
print w240.find("div", {"class": "title"}).h3.string
tab = w240.findAll("div", {"class": "tab"})

print tab[0].span.string
toplist = w240.findAll("div", {"class": "toplist ami"})
for url in toplist[0].findAll("a"):
    if url.get('class') == "down":
        print " x " + (url.get('href'))
        fakeurl = url.get('href')
        _get_d_url(fakeurl)
