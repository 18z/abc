class parser(object):

    def __init__(clipboard_content):

        content = clipboard_content


    def url(self, content):

        if content.startswith("http://") or content.startswith("https://") and not "bit.ly" in content:
            return True
        else:
            return False

__parser__ = parser()
