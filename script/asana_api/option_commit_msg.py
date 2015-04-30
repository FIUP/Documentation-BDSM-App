# -*- coding: utf-8 -*-
__author__ = 'ptesser'

from newapi import my_api
from asana import asana
import subprocess
import sys
import re


my_api_asana = my_api.MyAPI()

# FUNCTIONS


def fun_complete(id_str):
    id_int = int(id_str)
    my_api_asana.get_asana_api().update_task(id_int, completed=True)


def fun_delay(id_str):
    id_int = int(id_str)
    id_workspace_str = my_api_asana.get_id_workspace("mashup-unipd.it")
    id_tag_str = my_api_asana.get_id_tag(id_workspace_str, "DELAY")
    my_api_asana.get_asana_api().add_tag_task(id_int, id_tag_str)

options_cmd = {
    "complete": fun_complete,
    "delay": fun_delay
}

# END FUNCTIONS

if __name__ == '__main__':

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
                        id_task_str = id_task_re.group()[1:]

                if opt_match_re:
                    option_list = re.findall(r"\[[a-z]*\]", str(opt_match_re.group()), flags=0)
                    if option_list is not None:
                        for option in option_list:
                            option_msg_str = str(option)[1:-1]
                            if option_msg_str != "option" and id_task_str != "id_task":
                                try:
                                    options_cmd[option_msg_str](id_task_str)
                                except asana.AsanaException:
                                    checkout_asana_cmd = ["git", "checkout", "script/asana_api"]
                                    subprocess.call(checkout_asana_cmd)

    checkout_asana_cmd = ["git", "checkout", "script/asana_api"]
    subprocess.call(checkout_asana_cmd)
    sys.exit(0)