import inspect
import sys
import os
import androguard

print inspect.getsourcefile(os)


test = '123'


def teeee():
    import os
    jeeee = "456"
    # print jeeee
    # print locals()
    print globals()

# print globals()
# print "---------------"
# print locals()
teeee()

# print hello.g
