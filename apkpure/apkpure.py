import wget
import cookielib
import urllib2

import BeautifulSoup

jar = cookielib.FileCookieJar("cookies")

s = "https://apkpure.com/pocket-monster-remake/yoyo.Easy2play.now/download?from=category"
s1 = "https://download.apkpure.com/b/apk/Y29tLmFwa3B1cmUuYWVnb25fODgzXzQwMWUxNzkz?_fn=QVBLUHVyZV92MS4yLjVfYXBrcHVyZS5jb20uYXBr&k=7ffc496035ca1299ddd1a9914e3b23125896c445&as=cb462d8712e6f1ec8ee41298304e8238589421bd&_p=Y29tLmFwa3B1cmUuYWVnb24%3D&c=1%7CTOOLS"

def _get_d_url(durl):
    # durl = "http://m.apk.tw/app/com.android.vending/"
    # soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(durl))
    # dclass = soup.find("div", {"class": "download"})
    # print " o " + dclass.find("a").get('href')
    # dlink = dclass.find("a").get('href')
    # targetapk = urllib.urlopen(dlink)
    # targetapk = urllib.urlopen(durl)

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0')]
    response1 = opener.open(durl).geturl()
    print response1
    # response2 = opener.open(response1)
    # print type(response2.read())
    # print response2
    # target = urlopen(response1)

    filename = wget.download(response1)
    # print filename

    # with open('target.apk', 'wb') as output:
    #     output.write(target.read())

_get_d_url(s1)
