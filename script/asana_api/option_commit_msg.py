# -*- coding: utf-8 -*-
__author__ = 'ptesser'

from newapi import my_api
import subprocess
import sys


# MAIN

print "Execution script from branch: ", sys.argv[1]
print "List of commit message: "
print sys.argv[2]

list_commit_queue = sys.argv[2].split("END")
print list_commit_queue

for commit_msg in list_commit_queue:
    if commit_msg != "":  # per non eseguire le istruzioni sull'ultimo valore che è sempre vuoto
        print 1


checkout_asana_cmd = ["git", "checkout", "script/asana_api"]
subprocess.call(checkout_asana_cmd)