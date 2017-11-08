import os
import re

from viper.common.out import *
from viper.common.abstracts import Module
from viper.core.session import __session__

from androguard.core.bytecodes import apk, dvm

class Permissions(Module):
    cmd = 'lib'
    description = 'Extract libraries from file'

    def run(self):

        if not __session__.is_set():
            print_error("No session opened")
            return

        if os.path.exists(__session__.file.path):
            try:
                # data = open(__session__.file.path, 'r').read()
                a = apk.APK(__session__.file.path)
                # d = dvm.DalvikVMFormat(a.get_dex())
                print a.get_libraries()
                # print a.get_details_permissions()
                # print d.get_regex_strings("http")
            except (IOError, OSError) as e:
                print_error("Cannot open file: {0}".format(e))
