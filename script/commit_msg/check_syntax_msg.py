# -*- coding: utf-8 -*-
__author__ = 'ptesser'

import sys
import subprocess
# import re

print sys.argv[1]

checkout_commit_msg_cmd = ["git", "checkout", "script/commit_msg"]
subprocess.call(checkout_commit_msg_cmd)