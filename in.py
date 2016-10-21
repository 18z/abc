import inspect
import sys
import os
import androguard

# print inspect.getsourcefile(androguard)
if "site-packages" in inspect.getsourcefile(androguard):
    print "third party library"
else:
    print "standard library"

print inspect.getsourcefile(os)
# if "site-packages" in inspect.getsourcefile(sys):
#     print "third party library"
# else:
#     print "standard library"

# print sys.modules.keys()

import types


def imports():
    for name, val in globals().items():
        print name
        # if isinstance(val, types.ModuleType):
        # yield val.__name__
        # print val.__name__

imports

for i in range(0, len(globals().items())):
    print globals().items()[i][1]

# list(imports)
