class person(object):

    def __init__(self, width, length):
        self.width = width
        self.length = length


john = person("30", "150")
mary = person("20", "140")

people = [john, mary]

for p in people:
    print p.length
