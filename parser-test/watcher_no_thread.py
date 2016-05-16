import time
import threading
import pyperclip

from core.parser import __parser__
from core.plugins import __modules__

def process(clipboard_content):
    if __parser__.url(clipboard_content) is True:
        __modules__['print_url'].run(clipboard_content)
    else:
        print "print from watcher.run() "+clipboard_content

class ClipboardWatcher(object):
    def __init__(self, pause):
        self._pause = pause
        self._stopping = False

    def run(self):
        recent_value = ""
        while not self._stopping:
            if pyperclip.paste() != recent_value:
                recent_value = pyperclip.paste()
                process(recent_value)
            time.sleep(self._pause)

    def stop(self):
        self._stopping = True

if __name__ == "__main__":

    watcher = ClipboardWatcher(1)
    watcher.run()

    while True:
        try:
            # print "Waiting for changed clipboard..."
            time.sleep(5)
        except KeyboardInterrupt:
            watcher.stop()
            break
