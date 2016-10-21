import inspect
import os
import pprint
import androguard

print inspect.getsourcefile(androguard)
if "site-packages" in inspect.getsourcefile(androguard):
    print "third party library"
else:
    print "standard library"

print inspect.getsourcefile(os)
if "site-packages" in inspect.getsourcefile(os):
    print "third party library"
else:
    print "standard library"
