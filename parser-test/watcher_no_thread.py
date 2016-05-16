import time
import threading
import pyperclip

from core.parser import __parser__
from core.plugins import __modules__

class ClipboardWatcher(object):
    def __init__(self, pause):
        super(ClipboardWatcher, self).__init__()
        self._pause = pause
        self._stopping = False

    def run(self):
        recent_value = ""
        while not self._stopping:
            if pyperclip.paste() != recent_value:
                recent_value = pyperclip.paste()
                print "print from watcher.run() "+recent_value
                if __parser__.url(pyperclip.paste()) is True:
                    __modules__['print_url'].run(pyperclip.paste())
            time.sleep(self._pause)

    def stop(self):
        self._stopping = True

if __name__ == "__main__":

    watcher = ClipboardWatcher(1)
    watcher.run() # same as calling watcher.run()

    while True:
        try:
            # print "Waiting for changed clipboard..."
            time.sleep(5)
        except KeyboardInterrupt:
            watcher.stop()
            break
