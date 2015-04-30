#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name: nome_file.py
# Author: Tesser Paolo
# Date: aaaa-mm-dd
# Mail: p.tesser921@gmail.com
# Modify
# Version   Date        Author          Description
# =======================================================================
# 
# -----------------------------------------------------------------------
#
# -----------------------------------------------------------------------
#
#
__author__ = 'ptesser'
import re


class Componenti():
    """TODO

    Attributes:
        __base_path_str: TODO
        __client_base_path_str: TODO
        __server_base_path_str: TODO
        __doc_path_array: TODO
        __comp_array: TODO
        __write_list_comp_str: TODO
        __write_list_comp_file: TODO
    """
    __base_path_str = "../../documenti/specifica_tecnica/content/"
    __client_base_path_str = "/client_tier/"
    __server_base_path_str = "/server_tier/"

    __doc_path_array = [__base_path_str + __client_base_path_str + "model_data.tex",
                        __base_path_str + __client_base_path_str + "model_services.tex",
                        __base_path_str + __client_base_path_str + "view.tex",
                        __base_path_str + __client_base_path_str + "controller.tex",
                        __base_path_str + __server_base_path_str + "db.tex",
                        __base_path_str + __server_base_path_str + "endpoints.tex",
                        __base_path_str + __server_base_path_str + "miner.tex",
                        __base_path_str + __server_base_path_str + "processor.tex"
                        ]

    __comp_array = []

    __write_list_comp_str = ""
    __write_list_comp_file = ""

    def __init__(self):
        pass

    def take_componenti(self):
        """TODO

        Returns:
            TODO
        """

        for doc in self.__doc_path_array:
            doc_file = open(doc, "r")
            doc_file_line = [line.strip() for line in doc_file]
            doc_file.close()

            for line in doc_file_line:
                caso_match_re = re.match(r"^\\(subsubsection){.*}", line)
                if caso_match_re is not None:
                    caso = re.search(r"^(.*?){(.*?)}", caso_match_re.group())
                    if caso:
                        self.__comp_array.append(caso.group(2))

    def write_componenti(self):
        """TODO

        Returns:
            TODO
        """
        self.__write_list_comp_str = "componenti-requisiti-base.tex"
        self.__write_list_comp_file = open(self.__write_list_comp_str, "w")
        self.__write_list_comp_file.write("\subsection{Componenti-Requisiti} % (fold)\n")
        self.__write_list_comp_file.write("\label{sub:componenti_requisiti}\n")
        self.__write_list_comp_file.write("\\begin{center}\n")
        self.__write_list_comp_file.write("\def\\arraystretch{1.5}\n")
        self.__write_list_comp_file.write("\\bgroup\n")
        self.__write_list_comp_file.write("\\begin{longtable}{| p{9cm} | p{4cm} |}\n")
        self.__write_list_comp_file.write("\hline\n")
        self.__write_list_comp_file.write("\\textbf{Componente} & \\textbf{Requisiti} \\\\\n")
        self.__write_list_comp_file.write("\hline\n")

        for val in self.__comp_array:
            self.__write_list_comp_file.write(val + "  &  TO DO \\\\\n")
            self.__write_list_comp_file.write("\hline\n")

        self.__write_list_comp_file.write("\end{longtable}\n")
        self.__write_list_comp_file.write("\egroup\n")
        self.__write_list_comp_file.write("\end{center}\n")
        self.__write_list_comp_file.write("% subsection componenti_requisiti (end)\n")

if __name__ == '__main__':
    c = Componenti()
    c.take_componenti()
    c.write_componenti()