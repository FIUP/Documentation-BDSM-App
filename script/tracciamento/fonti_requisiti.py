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


class FontiRequisiti():
    """This class is used to tracks fonti to requisiti that generates it and viceversa

    Attributes:
        __req_doc_path_str: TODO
        __write_doc_path_str: TODO
        __req_doc_file: TODO
        __write_doc_file: TODO
        __req_file_line: TODO
        __fonti_req_dict: TODO
        __casi_uso_array: TODO
    """
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
        """TODO

        Args:
            fonti_req_dict_arg:
        """
        self.__fonti_req_dict = fonti_req_dict_arg

    def write_fonti_req(self):
        """TODO

        Returns:
            TODO
        """
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
        counter = 0
        for fonte_interno in fonti_interno:
            self.__write_doc_file.write(fonte_interno + " ")
            counter += 1
            if counter > 45:
                self.__write_doc_file.write("\\\\\n")
                self.__write_doc_file.write("\hline\n")
                self.__write_doc_file.write("Interno & ")
                counter = 0
            else:
                self.__write_doc_file.write("\\newline ")

        self.__write_doc_file.write("\\\\\n")
        self.__write_doc_file.write("\hline\n")

        # scrittura delle fonti degli Use Case

        for use_case in self.__casi_uso_array:

            if use_case in self.__fonti_req_dict:
                req_for_use_case = self.__fonti_req_dict[use_case]
                self.__write_doc_file.write(use_case + " & ")
                length = len(req_for_use_case)
                counter = 0
                for r in req_for_use_case:
                    self.__write_doc_file.write(r + " ")
                    counter += 1
                    if counter != length:
                        self.__write_doc_file.write("\\newline ")
            else:
                self.__write_doc_file.write(use_case + " & TO DO: Use Case non tracciato! ")

            self.__write_doc_file.write("\\\\\n")
            self.__write_doc_file.write("\hline\n")

        # scrittura delle fonti dei Verbali
        fonti_verbale = [(key, value) for key, value in self.__fonti_req_dict.iteritems() if key.startswith("Verbale")]
        for fonte_verbale in fonti_verbale:
            self.__write_doc_file.write(fonte_verbale[0] + " & ")
            length = len(fonte_verbale[1])
            counter = 0

            for req in fonte_verbale[1]:
                self.__write_doc_file.write(req + " ")
                counter += 1
                if counter != length:
                    self.__write_doc_file.write("\\newline ")

            self.__write_doc_file.write("\\\\\n")
            self.__write_doc_file.write("\hline\n")

        # chiusura struttura documento
        self.__write_doc_file.write("\end{longtable}\n")
        self.__write_doc_file.write("\egroup\n")
        self.__write_doc_file.write("\end{center}\n")
        self.__write_doc_file.write("% subsubsection fonti_requisiti (end)\n")

    def open_doc_fonti(self):
        """TODO

        Returns:
            TODO
        """
        self.__req_doc_path_str = "../../documenti/analisi_dei_requisiti/content/casi_uso.tex"
        self.__req_doc_file = open(self.__req_doc_path_str, "r")
        # mi salvo tutte le righe del file in una lista togliendoli il carattere di ritorno a capo
        self.__req_file_line = [line.strip() for line in self.__req_doc_file]
        # chiudo il file aperto per la lettura
        self.__req_doc_file.close()

    def set_casi_uso(self):
        """TODO

        Returns:
            TODO
        """
        for line in self.__req_file_line:
            caso_match_re = re.match(r"^\\(subsection|subsubsection){UC(.*?):", line)
            if caso_match_re is not None:
                caso = re.search(r"^(.*?)UC(.*?):", caso_match_re.group())
                if caso:
                    # aggiorno l'array solo dei requisiti
                    self.__casi_uso_array.append("UC" + caso.group(2))

    def get_list_fonti(self):
        """TODO

        Returns:
            TODO
        """
        return self.__fonti_req_dict

    def get_array_casi_uso(self):
        """TODO

        Returns:
            TODO
        """
        return self.__casi_uso_array