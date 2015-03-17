#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name: requisiti-fonti.py
# Author: Tesser Paolo
# Date: 2015-03-17
# Mail: p.tesser921@gmail.com
# Modify
# Version   Date        Author          Description
# =======================================================================
# 0.0.1     2015-03-17  Tesser Paolo    codifica script
# -----------------------------------------------------------------------
#
# -----------------------------------------------------------------------
#
#
__author__ = 'ptesser'
import re
import os
import sys


class RequisitiFonti():

    __req_doc_path_str = ""
    __req_doc_file = ""
    __req_file_line = []
    __fonti_req_dict = {}
    __req_fonti_dict = {}

    def __init__(self):
        pass

    def open_doc_req(self):
        self.__req_doc_path_str = "../../documenti/analisi_dei_requisiti/content/requisiti.tex"
        self.__req_doc_file = open(self.__req_doc_path_str, "r")
        self.__req_file_line = [line.strip() for line in self.__req_doc_file]
        # mi salvo tutte le righe del file in una lista togliendoli il carattere di ritorno a capo
        self.__req_doc_file.close()

    def get_list_fonti(self):
        for line in self.__req_file_line:
            req_match_re = re.match(r"^R(.*)", line)
            if req_match_re is not None:
                req = re.search(r"^R(.*)&", line)
                if req:
                    print req.group()

if __name__ == '__main__':
    print "Test"

    test_dict = {}

    test_dict.update({'ROF2': {"Interno", "UC2"}})
    test_dict.update({'ROF3': {"Interno", "UC2"}})
    test_dict.update({'ROF4': {"Interno", "UC2"}})

    for key, value in test_dict.iteritems():
        print "======="
        print "Requisito: " + key
        print "-------"
        for el in value:
            print "Fonte: " + el
        print "======="

    f = RequisitiFonti()
    f.open_doc_req()
    f.get_list_fonti()