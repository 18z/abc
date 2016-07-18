# import logging
from datetime import datetime
# from progress.bar import Bar

from core.db.Mongo import DB
from common.objects import File
# from common.helpers import sizeof_fmt, print_header_line, print_result_line

import urllib
import BeautifulSoup

s1 = "http://m.apk.tw/top"

today = datetime.now().strftime('%Y-%m-%d')

soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(s1))


def insert_into_db(result):
    DB().insert_apk(result)


def generate_apk_info(targetapk, rank):

    result = {}
    result['vt_scan'] = False
    result['submit_date'] = today
    result['source'] = 'm.apk'
    result['title'] = category
    result['sub_title'] = subcategory
    result['name'] = unicode(apk_name).encode('utf8')
    result['rank'] = rank
    result['pgname'] = pkg_name
    result['version'] = version
    result['size'] = size
    result['upload_date'] = ""

    # Download APK
    result['apkdata'] = targetapk.read()

    # Calculate file hashes
    result.update(File(result['apkdata']).result)

    print ' N ' + result['name']
    print ' V ' + result['version']
    print ' M ' + result['md5']
    print ' S ' + result['size']
    print ' P ' + result['pgname'] + "\n"

    return result


def _download_apk(dlink):
    targetapk = urllib.urlopen(dlink)
    return targetapk


def _get_d_url(durl):
    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(durl))
    dclass = soup.find("div", {"class": "download"})
    print " o " + dclass.find("a").get('href')
    dlink = dclass.find("a").get('href')

    return dlink


def _get_apk_name(durl):
    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(durl))
    title = soup.find("div", {"class": "detailInfo mt-5"})
    apk_name = title.find("h3").string

    return apk_name


def _get_apk_attr(durl):
    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(durl))
    ppt = soup.find("div", {"class": "property mt-10"})
    ppts = ppt.findAll("li")
    version = ppts[0].string
    size = ppts[1].string

    return version, size


# category
w240 = soup.findAll("div", {"class": "w240 mt-12 mr-15"})[0]
category = w240.find("div", {"class": "title"}).h3.string
print category

# sub-category
tab = w240.findAll("div", {"class": "tab"})
subcategory = tab[0].span.string
print subcategory

# download list
toplist = w240.findAll("div", {"class": "toplist ami"})

rank = 1
for url in toplist[0].findAll("a"):
    if url.get('class') == "down":
        # slicing package name
        pkg_name = url.get('href')[20:][:-1]

        fakeurl = url.get('href')
        dlink = _get_d_url(fakeurl)
        targetapk = _download_apk(dlink)
        apk_name = _get_apk_name(fakeurl)
        version, size = _get_apk_attr(fakeurl)
        result = generate_apk_info(targetapk, rank)
        insert_into_db(result)
        rank += 1
