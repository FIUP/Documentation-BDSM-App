# -*- coding: utf-8 -*-
__author__ = 'ptesser'

from newapi import my_api
import subprocess
import sys
import re

# MAIN
my_api_asana = my_api.MyAPI()

print "Execution script from branch: ", sys.argv[1]
# print "List of commit message: "
# print sys.argv[2]

list_commit_queue = sys.argv[2].split("END")
# print list_commit_queue

for commit_msg in list_commit_queue:
    if commit_msg != "":  # per non eseguire le istruzioni sull'ultimo valore che è sempre vuoto
        list_message = commit_msg.splitlines()  # separo ogni riga del messaggio quando trovo il carattere \n
        id_task_str = ""
        option_list = []

        for line in list_message:  # scorro tutte le linee trovate
            task_match_re = re.match(r"^Task(.*)", line.strip())  # mi salvo la riga che inizia con 'Task'
            opt_match_re = re.match(r"^Option(.*)", line.strip())  # mi salvo la riga che inizia con 'Option'

            if task_match_re:
                id_task_re = re.search(r"#(.*)", str(task_match_re.group()))
                if id_task_re is not None:
                    id_task_str = id_task_re.group()
                    print id_task_str

            if opt_match_re:
                option_list_re = re.findall(r"\[[a-z]*\]", str(opt_match_re.group()), flags=0)
                if option_list_re is not None:
                    print option_list_re

checkout_asana_cmd = ["git", "checkout", "script/asana_api"]
subprocess.call(checkout_asana_cmd)