#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name: fonti-requisiti.py
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


class FontiRequisiti():

    __req_doc_path_str = ""
    __write_doc_path_str = ""

    __req_doc_file = ""
    __write_doc_file = ""

    __req_file_line = []

    __fonti_req_dict = {}
    __casi_uso_array = []

    def __init__(self):
        pass

    def add_fonti_req(self, fonti_req_dict_arg):
        self.__fonti_req_dict = fonti_req_dict_arg

    def write_fonti_req(self):
        self.__write_doc_path_str = "fonti-requisiti.tex"
        self.__write_doc_file = open(self.__write_doc_path_str, "w")

        self.__write_doc_file.write("\subsection{Fonti-Requisiti} % (fold)\n")
        self.__write_doc_file.write("\label{ssub:fonti_requisiti}\n")
        self.__write_doc_file.write("\\begin{center}\n")
        self.__write_doc_file.write("\def\\arraystretch{1.5}\n")
        self.__write_doc_file.write("\\bgroup\n")
        self.__write_doc_file.write("\\begin{longtable}{| p{4cm} | p{4cm} |}\n")
        self.__write_doc_file.write("\hline\n")
        self.__write_doc_file.write("\\textbf{Fonte} & \\textbf{Requisiti derivati} \\\\\n")
        self.__write_doc_file.write("\hline\n")

        # scrittura delle fonti interne
        fonti_interno = self.__fonti_req_dict["Interno"]
        self.__write_doc_file.write("Interno & ")
        for fonte_interno in fonti_interno:
            self.__write_doc_file.write(fonte_interno + " \\newline ")

        self.__write_doc_file.write("\\\\\n")
        # scrittura delle fonti degli Use Case
        
        # scrittura delle fonti dei Verbali
        self.__write_doc_file.write("\end{longtable}\n")
        self.__write_doc_file.write("\egroup\n")
        self.__write_doc_file.write("\end{center}\n")
        self.__write_doc_file.write("% subsubsection fonti_requisiti (end)\n")

    def open_doc_fonti(self):
        self.__req_doc_path_str = "../../documenti/analisi_dei_requisiti/content/casi_uso.tex"
        self.__req_doc_file = open(self.__req_doc_path_str, "r")
        # mi salvo tutte le righe del file in una lista togliendoli il carattere di ritorno a capo
        self.__req_file_line = [line.strip() for line in self.__req_doc_file]
        # chiudo il file aperto per la lettura
        self.__req_doc_file.close()

    def set_casi_uso(self):
        for line in self.__req_file_line:
            caso_match_re = re.match(r"^\\(subsection|subsubsection){UC(.*?):", line)
            if caso_match_re is not None:
                caso = re.search(r"^(.*?)UC(.*?):", caso_match_re.group())
                if caso:
                    # aggiorno l'array solo dei requisiti
                    self.__casi_uso_array.append("UC" + caso.group(2))

    def get_list_fonti(self):
        return self.__fonti_req_dict

    def get_array_casi_uso(self):
        return self.__casi_uso_array