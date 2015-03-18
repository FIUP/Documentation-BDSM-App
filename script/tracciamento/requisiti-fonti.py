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
    __write_doc_path_str = ""

    __req_doc_file = ""
    __write_doc_file = ""

    __req_file_line = []
    __req_fonti_array = []

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

    def take_req(self):
        for line in self.__req_file_line:
            req_match_re = re.match(r"^R(.*)", line)
            if req_match_re is not None:
                req = re.search(r"^R(.*?)\s", line)
                if req:
                    fonti_for_req_array = line.split('&')[2].strip()
                    self.__req_fonti_dict.update({req.group(): fonti_for_req_array})
                    self.__req_fonti_array.append(req.group())

    def get_list_req(self):
        return self.__req_fonti_dict

    def write_req_fonti(self):
        self.__write_doc_path_str = "requisiti-fonti.tex"
        self.__write_doc_file = open(self.__write_doc_path_str, "w")
        self.__write_doc_file.write("\subsection{Requisiti-Fonti} % (fold)\n")
        self.__write_doc_file.write("\label{ssub:requisiti_fonti}\n")
        self.__write_doc_file.write("\\begin{center}\n")
        self.__write_doc_file.write("\def\\arraystretch{1.5}\n")
        self.__write_doc_file.write("\\bgroup\n")
        self.__write_doc_file.write("\\begin{longtable}{| p{4cm} | p{4cm} |}\n")
        self.__write_doc_file.write("\hline\n")
        self.__write_doc_file.write("\\textbf{Requisito} & \\textbf{Fonti} \\\\\n")
        self.__write_doc_file.write("\hline\n")

        for val in self.__req_fonti_array:
            fonti_val = self.__req_fonti_dict[val]
            self.__write_doc_file.write(val + "  &  " + fonti_val + "\n")
            self.__write_doc_file.write("\hline\n")

        self.__write_doc_file.write("\end{longtable}\n")
        self.__write_doc_file.write("\egroup\n")
        self.__write_doc_file.write("\end{center}\n")
        self.__write_doc_file.write("% subsubsection requisiti_fonti (end)\n")


if __name__ == '__main__':
    print "*** Start: script tracciamento requisiti-fonti ***"
    f = RequisitiFonti()
    f.open_doc_req()
    f.take_req()
    f.write_req_fonti()
    print "*** End: script tracciamento requisiti-fonti ***"