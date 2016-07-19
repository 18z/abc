# -*- coding: UTF-8 -*-
from datetime import datetime
import urllib
import BeautifulSoup

s1 = "http://m.apk.tw/top"

today = datetime.now().strftime('%Y-%m-%d')

soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(s1))


def _get_apk_name(durl):
    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(durl))
    title = soup.find("div", {"class": "detailInfo mt-5"})
    apk_name = title.find("h3").string

    return apk_name


def _get_apk_attr(durl):
    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(durl))
    ppt = soup.find("div", {"class": "property mt-10"})
    ppts = ppt.findAll("li")
    version = ppts[0].string.replace(u'版本：', "", 2)
    version = version.replace(":", "")
    version = version.replace(u'版本:', "")
    version = version.replace(u'版本', "")
    size = ppts[1].string

    return version, size

for cat in range(0, 6):
    # category
    w240 = soup.findAll("div", {"class": "w240 mt-12 mr-15"})[cat]
    category = w240.find("div", {"class": "title"}).h3.string
    print category

    for ts in range(0, 2):
        # sub-category
        tab = w240.findAll("div", {"class": "tab"})
        spans = w240.findAll('span')
        # print subcategory
        print spans[ts].string

        # download list
        toplist = w240.findAll("div", {"class": "toplist ami"})

        for url in toplist[ts].findAll("a"):
            if url.get('class') == "down":
                # slicing package name
                # pkg_name = url.get('href')[20:][:-1]

                fakeurl = url.get('href')
                # dlink = _get_d_url(fakeurl)
                # targetapk = _download_apk(dlink)
                apk_name = _get_apk_name(fakeurl)
                version, size = _get_apk_attr(fakeurl)
                print "\t" + apk_name + version
