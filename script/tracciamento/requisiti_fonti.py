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
# 0.0.2     2015-03-18  Tesser Paolo    terminato script con scrittura tracciamento su documento requisiti-fonti.tex
# -----------------------------------------------------------------------
# 0.0.3     2015-04-15  Tesser Paolo    aggiunto metodo per generare in un file tex, la lista dei requisiti
# -----------------------------------------------------------------------
#
__author__ = 'ptesser'
import re


class RequisitiFonti():
    """This class is used to tracks requisiti to fonti that generates it and viceversa

    Attributes:
        __req_doc_path_str: TODO
        __comp_doc_path_str: TODO
        __write_doc_path_str: TODO
        __write_list_req_str: TODO
        __req_doc_file: TODO
        __comp_doc_file: TODO
        __write_do_file: TODO
        __write_list_req_str: TODO
        __req_file_ine: TODO
        __comp_file_line: TODO
        __req_fonti_array: TODO
        __fonti_req_dict: TODO
        __req_fonti_dict: TODO
        __req_comp_dict: TODO

    """
    __req_doc_path_str = ""
    __comp_doc_path_str = ""
    __write_doc_path_str = ""
    __write_list_req_str = ""

    __req_doc_file = ""
    __comp_doc_file = ""
    __class_doc_file = ""
    __write_doc_file = ""
    __write_list_req_comp_file = ""
    __write_list_req_classi_file = ""

    __req_file_line = []
    __comp_file_line = []
    __class_file_line = []
    # array di soli requisiti per poterli scorrere dal primo all'ultimo nell'ordine di inserimento
    __req_array = []

    # dizionario per fare il tracciamento inverso fonti-requisiti
    __fonti_req_dict = {}
    # dizionario per ricavarmi le fonti sapendo il requisito come chiave
    __req_fonti_dict = {}
    # dizionario per ricavarmi i componenti sapendo il requisito come chiave
    __req_comp_dict = {}
    # dizionario per ricavarmi le classi sapendo il componente come chiave
    __classi_req_dict = {}

    def __init__(self):
        pass

    def open_doc_req(self):
        """TODO

        Returns:
            TODO
        """

        self.__req_doc_file = open("../../documenti/analisi_dei_requisiti/content/requisiti.tex", "r")
        self.__req_file_line = [line.strip() for line in self.__req_doc_file]
        # mi salvo tutte le righe del file in una lista togliendoli il carattere di ritorno a capo
        self.__req_doc_file.close()

    def open_doc_componenti(self):
        """TODO

        Returns:
            TODO
        """
        self.__comp_doc_file = open("../../documenti/specifica_tecnica/content/tracciamento/componenti-requisiti.tex",
                                    "r")
        self.__comp_file_line = [line.strip() for line in self.__comp_doc_file]
        # mi salvo tutte le righe del file in una lista togliendoli il carattere di ritorno a capo
        self.__comp_doc_file.close()

    def open_doc_classi(self):
        """TODO

        Returns:
            TODO
        """
        self.__class_doc_file = open("../../documenti/specifica_tecnica/content/tracciamento/componenti-requisiti.tex",
                                     "r")
        self.__class_file_line = [line.strip() for line in self.__comp_doc_file]
        # mi salvo tutte le righe del file in una lista togliendoli il carattere di ritorno a capo
        self.__class_doc_file.close()

    ########################

    def take_req(self):
        """TODO

        Returns:
            TODO
        """
        for line in self.__req_file_line:
            req_match_re = re.match(r"^R(.*)", line)
            if req_match_re is not None:
                req = re.search(r"^R(.*?)\s", line)
                if req:
                    fonti_for_req_array = line.split('&')[2].strip()
                    fonti_single_array = fonti_for_req_array[:-2].strip().split("\\newline")
                    # aggiorno il dizionario con il nuovo valore del requisito e le sue fonti
                    self.__req_fonti_dict.update({req.group(): fonti_for_req_array})
                    # aggiorno l'array solo dei requisiti
                    self.__req_array.append(req.group())

                    for fonte in fonti_single_array:
                        if fonte.strip() in self.__fonti_req_dict:
                            self.__fonti_req_dict[fonte.strip()].append(req.group().strip())
                        else:
                            self.__fonti_req_dict[fonte.strip()] = [req.group().strip()]

    def take_req_comp(self):
        """TODO

        Returns:
            TODO
        """
        for line in self.__comp_file_line:
            comp_match_re = re.match(r"^(server|client)", line)

            if comp_match_re is not None:
                # comp = re.search(r"^(server|client)(.*)", line)
                # print comp.group()
                comp = re.search(r"^(server|client)(.*)&", line)
                comp = (comp.group(1) + comp.group(2)).strip()
                if comp:
                    # TODO: change name
                    fonti_for_req_array = line.split('&')[1].strip()
                    # print fonti_for_req_array
                    fonti_single_array = fonti_for_req_array[:-1].strip().split("\\newline")
                    for req in fonti_single_array:
                        # print req.strip()
                        if req.strip() in self.__req_comp_dict:
                            self.__req_comp_dict[req.strip()].append(comp.strip())
                        else:
                            self.__req_comp_dict[req.strip()] = [comp.strip()]

    def get_list_req(self):
        """TODO

        Returns:
            TODO
        """
        return self.__req_fonti_dict

    def get_list_fonti(self):
        """TODO

        Returns:
            TODO
        """
        return self.__fonti_req_dict

    def write_req_fonti(self):
        """TODO

        Returns:
            TODO
        """
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

        for val in self.__req_array:
            fonti_val = self.__req_fonti_dict[val]
            self.__write_doc_file.write(val + "  &  " + fonti_val + "\n")
            self.__write_doc_file.write("\hline\n")

        self.__write_doc_file.write("\end{longtable}\n")
        self.__write_doc_file.write("\egroup\n")
        self.__write_doc_file.write("\end{center}\n")
        self.__write_doc_file.write("% subsubsection requisiti_fonti (end)\n")

    def write_list_req_for_comp(self):
        """This method write all requirements in the left column and set them components associated.
        If there aren't components a TODO it's set

        Returns:
            TODO
        """
        self.__write_list_req_str = "requisiti-componenti-base.tex"
        self.__write_list_req_comp_file = open(self.__write_list_req_str, "w")
        self.__write_list_req_comp_file.write("\subsection{Requisiti-Componenti} % (fold)\n")
        self.__write_list_req_comp_file.write("\label{sub:componenti_requisiti}\n")
        self.__write_list_req_comp_file.write("\\begin{center}\n")
        self.__write_list_req_comp_file.write("\def\\arraystretch{1.5}\n")
        self.__write_list_req_comp_file.write("\\bgroup\n")
        self.__write_list_req_comp_file.write("\\begin{longtable}{| p{4cm} | p{8cm} |}\n")
        self.__write_list_req_comp_file.write("\hline\n")
        self.__write_list_req_comp_file.write("\\textbf{Requisito} & \\textbf{Componenti} \\\\\n")
        self.__write_list_req_comp_file.write("\hline\n")

        for val in self.__req_array:
            val = val.strip()
            if val in self.__req_comp_dict:
                comp_for_req = self.__req_comp_dict[val]
                self.__write_list_req_comp_file.write(val + " & ")
                length = len(comp_for_req)
                counter = 0
                for r in comp_for_req:
                    self.__write_list_req_comp_file.write(r + " ")
                    counter += 1
                    if counter != length:
                        self.__write_list_req_comp_file.write("\\newline ")
            else:
                self.__write_list_req_comp_file.write(val + " & TO DO: Requisito non tracciato con nessun componente! ")

            self.__write_list_req_comp_file.write("\\\\\n")
            self.__write_list_req_comp_file.write("\hline\n")

        self.__write_list_req_comp_file.write("\end{longtable}\n")
        self.__write_list_req_comp_file.write("\egroup\n")
        self.__write_list_req_comp_file.write("\end{center}\n")
        self.__write_list_req_comp_file.write("% subsection componenti_requisiti (end)\n")

    def write_list_req_for_class(self):
        """This method write all requirements in the left column and left empty right column with a TODO marker.

        Returns:
            TODO
        """
        self.__write_list_req_str = "requisiti-classi-base.tex"
        self.__write_list_req_classi_file = open(self.__write_list_req_str, "w")
        self.__write_list_req_classi_file.write("\subsection{Requisiti-Componenti} % (fold)\n")
        self.__write_list_req_classi_file.write("\label{sub:componenti_requisiti}\n")
        self.__write_list_req_classi_file.write("\\begin{center}\n")
        self.__write_list_req_classi_file.write("\def\\arraystretch{1.5}\n")
        self.__write_list_req_classi_file.write("\\bgroup\n")
        self.__write_list_req_classi_file.write("\\begin{longtable}{| p{4cm} | p{8cm} |}\n")
        self.__write_list_req_classi_file.write("\hline\n")
        self.__write_list_req_classi_file.write("\\textbf{Requisito} & \\textbf{Classi} \\\\\n")
        self.__write_list_req_classi_file.write("\hline\n")

        for val in self.__req_array:
            val = val.strip()
            if val in self.__req_comp_dict:
                comp_for_req = self.__req_comp_dict[val]
                self.__write_list_req_classi_file.write(val + " & ")
                length = len(comp_for_req)
                counter = 0
                for r in comp_for_req:
                    self.__write_list_req_classi_file.write(r + " ")
                    counter += 1
                    if counter != length:
                        self.__write_list_req_classi_file.write("\\newline ")
            else:
                self.__write_list_req_classi_file.write(val + " & TO DO: Requisito non tracciato con nessuna classe! ")

            self.__write_list_req_classi_file.write("\\\\\n")
            self.__write_list_req_classi_file.write("\hline\n")

        self.__write_list_req_classi_file.write("\end{longtable}\n")
        self.__write_list_req_classi_file.write("\egroup\n")
        self.__write_list_req_classi_file.write("\end{center}\n")
        self.__write_list_req_classi_file.write("% subsection componenti_requisiti (end)\n")