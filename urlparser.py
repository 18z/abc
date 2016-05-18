import re

URL_REGEX = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
IPV4_REGEX = re.compile('[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]')
DOMAIN_REGEX = re.compile('([a-z0-9][a-z0-9\-]{0,61}[a-z0-9]\.)+[a-z0-9][a-z0-9\-]*[a-z0-9]', re.IGNORECASE)

# hosts = IPV4_REGEX.findall("8.8.8.8+4.4.4.4+10.3.60.2")
# domains = DOMAIN_REGEX.findall("www.google.com.tw, tw.yahoo.com, www.icst.org.tw")
# urls = URL_REGEX.findall('<p>Hello World</p><a href="http://example.com">More Examples</a><a href="http://example2.com">Even More Examples</a>+http://www.goog.ecom.tw')


textfile = open("filename.txt", 'r')
filetext = textfile.read()
# textfile.close()

hosts = IPV4_REGEX.findall(filetext)

print hosts
# print domain
# print urls
