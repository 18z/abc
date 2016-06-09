import urllib
import BeautifulSoup

s1 = "http://amtrckr.info/"
soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(s1))
[s.extract() for s in soup('i')]

tables = soup.findAll('table')
my_table = tables[0]

rows = my_table.findAll(['th', 'tr'])
for row in rows:
    cells = row.findAll('td')
    for cell in cells:
        if cell.string:
            print str(cell.string).split("&nbsp;", 1)[0].strip()
        elif cell.a:
            # if cell.a.string:
            #     print str(cell.a.string).split("&nbsp;", 1)[0]
            if cell.a.get('href'):
                print str(cell.a.get('href'))
            elif cell.a.string:
                print str(cell.a.string).split("&nbsp;", 1)[0]

    print "-=-=-=-=-=-=-=-=-=-"
