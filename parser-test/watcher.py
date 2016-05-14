from parser import __parser__
from plugins import __modules__

clipboard_content = "http://www.google.com.tw"

# print __parser__.url(clipboard_content)

if __parser__.url(clipboard_content) is True:
    __modules__['print_url'].run(clipboard_content)
