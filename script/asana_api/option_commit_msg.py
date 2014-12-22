# -*- coding: utf-8 -*-
__author__ = 'ptesser'

from newapi import my_api
import subprocess
import sys


# MAIN
my_api_asana = my_api.MyAPI()

print "Execution script from branch: ", sys.argv[1]
# print "List of commit message: "
# print sys.argv[2]

list_commit_queue = sys.argv[2].split("END")
# print list_commit_queue

for commit_msg in list_commit_queue:
    if commit_msg != "":  # per non eseguire le istruzioni sull'ultimo valore che è sempre vuoto
        list_message = commit_msg.splitlines()
        for line in list_message:
            line.trim()
            print line

checkout_asana_cmd = ["git", "checkout", "script/asana_api"]
subprocess.call(checkout_asana_cmd)