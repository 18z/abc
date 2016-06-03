class suite(object):

    umbrella = "black_unbrella"

    def __init__(self, tshirt_size, shoe_size, pant_size):
        self.tshirt = tshirt_size
        self.shoes = shoe_size
        self.pant = pant_size

    def show_suite(self):
        print (self.tshirt, self.shoes, self.pant)


s = suite("M", "10.5", "33")

s.show_suite()
print(s.umbrella)
