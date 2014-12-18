__author__ = 'ptesser'

from newapi import my_api
from date import date
import subprocess
import sys

# branch_name_cmd = ["git", "rev-parse", "--abbrev-ref", "HEAD"]
# branch_name = subprocess.Popen(branch_name_cmd, stdout=subprocess.PIPE, shell=True)
# (output, err) = branch_name.communicate()
# print "Branch name from py: ", branch_name

# MAIN

print "Branch name from bash: ", sys.argv[1]
print "List of commit message: ", sys.argv[2]

