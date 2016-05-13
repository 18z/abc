from parser import __parser__
from plugins import __modules__

clipboard_content = "http://www.google.com.tw"

# print __parser__.url(clipboard_content)

if __parser__.url(clipboard_content) is True:
    print __modules__.run(clipboard_content)
