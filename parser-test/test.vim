function! Sixense()

    python << EOF
import vim
import time
import pyperclip
import sys
sys.path.append('/home/deanboole/Documents/abc/parser-test')

from core.parser import __parser__
from core.plugins import __modules__

clipboard_content = pyperclip.paste()

def process(clipboard_content):

    if __parser__.url(clipboard_content) is True:
        __modules__['print_url'].run(clipboard_content)
    elif __parser__.timestamp(clipboard_content) is True:
        __modules__['print_timestamp'].run(clipboard_content)
    else:
        print clipboard_content + " ----->>  not in patterns"


process(clipboard_content)

EOF


endfunc
