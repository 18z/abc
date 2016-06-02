class suite(object):

    umbrella = "black_unbrella"

    def __init__(self):
        self.tshirt = "sizeM"
        self.shoes = "9.5"
        self.pant = "30"

    def show_suite(self):
        print (self.tshirt, self.shoes, self.pant)


s = suite()

s.show_suite()
print(s.umbrella)
