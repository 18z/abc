import os
import re

from viper.common.out import *
from viper.common.abstracts import Module
from viper.core.session import __session__

from androguard.core.bytecodes import apk

class Permissions(Module):
    cmd = 'perm'
    description = 'Extract permissions from file'

    def run(self):

        if not __session__.is_set():
            print_error("No session opened")
            return

        if os.path.exists(__session__.file.path):
            try:
                # data = open(__session__.file.path, 'r').read()
                a = apk.APK(__session__.file.path)
                print a.get_app_name()
                print a.get_details_permissions()
            except (IOError, OSError) as e:
                print_error("Cannot open file: {0}".format(e))
