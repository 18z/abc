# import logging
# import argparse
from datetime import datetime, timedelta
# from progress.bar import Bar

# from core.config import import *

# from core.db.MongoMongo import DB
from common.objects import File
# from common.helpers import sizeof_fmt, print_header_line, print_result_line

import urllib
import BeautifulSoup

s = "http://m.apk.tw"
s1 = "http://m.apk.tw/top"

today = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(s1))


def generate_apk_info(targetapk):
    result = {}
    result['vt_scan'] = False
    result['submit_date'] = today
    result['source'] = 'm.apk'
    # result['title'] = cat
    # result['sub_title'] = ctr
    # result['name'] = unicode(i.title).encode('utf8')
    # result['rank'] = rank
    # result['pgname'] = i.details.appDetails.packageName
    # result['version'] = i.details.appDetails.versionCode
    # result['size'] = sizeof_fmt(i.details.appDetails.installationSize)
    # result['upload_date'] = datetime.strptime(unicode(i.details.appDetails.uploadDate).encode('utf8'),
    #                                           locale_timestring[LANG]).strftime('%Y-%m-%d')
    # Download APK
    result['apkdata'] = targetapk.read()

    # Calculate file hashes
    result.update(File(result['apkdata']).result)

    print result['md5']


def _download_apk(dlink):
    targetapk = urllib.urlopen(dlink)
    generate_apk_info(targetapk)
    # with open('target.apk', 'wb') as output:
    #     output.write(targetapk.read())


def _get_d_url(durl):
    # durl = "http://m.apk.tw/app/com.android.vending/"
    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(durl))
    dclass = soup.find("div", {"class": "download"})
    print " o " + dclass.find("a").get('href')
    dlink = dclass.find("a").get('href')
    _download_apk(dlink)

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
