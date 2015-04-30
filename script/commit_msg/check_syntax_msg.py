# -*- coding: utf-8 -*-
__author__ = 'ptesser'

import sys
import subprocess
import re

if __name__ == '__main__':

    commit_mg_file = open(sys.argv[1])  # apro il file che ricevo come path dall'invocazione dello script
    lines = [line.strip() for line in commit_mg_file]  # mi salvo tutte le righe del file in una lista togliendoli
    # il carattere di ritorno a capo

    commit_mg_file.close()  # chiudo il file aperto in lettura

    # variabili da controllare
    check_title_bool = False
    check_desc_bool = False
    check_task_bool = False
    check_option_bool = False
    check_end_bool = False
    error_msg_str = ""

    for line in lines:
        title_match_re = re.match(r"^Title:(.*)", line)
        desc_match_re = re.match(r"^Desc:(.*)", line)
        task_match_re = re.match(r"^Task: Reported in #(.*)", line)  # mi salvo la riga che inizia con 'Task'
        opt_match_re = re.match(r"^Option:(.*)", line)  # mi salvo la riga che inizia con 'Option'
        end_match_re = re.match(r"^END", line)
        if title_match_re is not None:
            check_title_bool = True
        if desc_match_re is not None:
            check_desc_bool = True
        if task_match_re is not None:
            check_task_bool = True
        if opt_match_re is not None:
            check_option_bool = True
        if end_match_re is not None:
            check_end_bool = True

    if not check_title_bool or not check_desc_bool or not check_task_bool or not check_option_bool or not check_end_bool:
        print "WARNING! Messaggio di commit di forma errata."
        print error_msg_str, "MANCANTE/I"
        checkout_commit_msg_cmd = ["git", "checkout", "script/commit_msg"]
        subprocess.call(checkout_commit_msg_cmd)
        sys.exit(1)

    print "OK. Formato messaggio di commit corretto."
    checkout_commit_msg_cmd = ["git", "checkout", "script/commit_msg"]
    subprocess.call(checkout_commit_msg_cmd)
    sys.exit(0)