#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def get_doc_classi_file_line():
    doc_classi_file_line = []
    base_path_str = "../../documenti/definizione_di_prodotto/content/"
    client_base_path_str = "/client_tier/"
    server_base_path_str = "/server_tier/"

    doc_path_array = [base_path_str + client_base_path_str + "model_data.tex",
                      base_path_str + client_base_path_str + "model_services.tex",
                      base_path_str + client_base_path_str + "view.tex",
                      base_path_str + client_base_path_str + "controller.tex",
                      base_path_str + server_base_path_str + "db.tex",
                      base_path_str + server_base_path_str + "endpoints.tex",
                      base_path_str + server_base_path_str + "miner.tex",
                      base_path_str + server_base_path_str + "processor.tex"
                      ]

    for doc in doc_path_array:
        doc_classi_file = open(doc, "r")
        doc_classi_file_line.extend([line.strip() for line in doc_classi_file])
        doc_classi_file.close()

    # print doc_classi_file_line
    return doc_classi_file_line


# This function takes all class in the files that describe the architecture: Definizione di Prodotto
def get_classi_array(doc_classi_file_line):

    classi_array = []

    for line in doc_classi_file_line:
        caso_match_re = re.match(r"^\\(subparagraph){.*}", line)
        if caso_match_re is not None:
            caso = re.search(r"^(.*?){(.*?)}", caso_match_re.group())
            if caso:
                classi_array.append(caso.group(2))

    return classi_array


# This function saves class like key and requirements like values in a dictionary
def get_classi_req_dict(doc_classi_file_line):

    classi_req_dict = {}
    classi_for_req_array = []
    classi_single_array = []

    for line in doc_classi_file_line:
        comp_match_re = re.match(r"^(R)", line)

        if comp_match_re is not None:
            # comp = re.search(r"^(server|client)(.*)", line)
            # print comp.group()
            comp = re.search(r"^(R)(.*)&", line)
            comp = (comp.group(1) + comp.group(2)).strip()
            if comp:

                classi_for_req_array = line.split('&')[1].strip()
                classi_single_array = classi_for_req_array[:-1].strip().split("\\newline")
                for req in classi_single_array:
                    if req.strip() in classi_req_dict:
                        classi_req_dict[req.strip()].append(comp.strip())
                    else:
                        classi_req_dict[req.strip()] = [comp.strip()]

    return classi_req_dict


# This function prints a table with the class in the left column, the list of classi and in the second column the req
# getted from the table in requisiti-classi.tex file
def print_classi_req():
    file_classi_req = open("classi-requisiti.tex", "w")
    doc_classi_file_line = get_doc_classi_file_line()
    classi_req_dict = get_classi_req_dict(doc_classi_file_line)
    classi_array = get_classi_array(doc_classi_file_line)

    file_classi_req.write("\subsection{Classi-Requisiti} % (fold)\n")
    file_classi_req.write("\label{sub:classi_requisiti}\n")
    file_classi_req.write("\\begin{center}\n")
    file_classi_req.write("\def\\arraystretch{1.5}\n")
    file_classi_req.write("\\bgroup\n")
    file_classi_req.write("\\begin{longtable}{| p{9cm} | p{3cm} |}\n")
    file_classi_req.write("\hline\n")
    file_classi_req.write("\\textbf{Classi} & \\textbf{Requisiti} \\\\\n")
    file_classi_req.write("\hline\n")

    for classe in classi_array:
        classe = classe.strip()
        # TODO: refactor with real code
        file_classi_req.write(classe + " & TO DO ")
        file_classi_req.write("\\\\\n")
        file_classi_req.write("\hline\n")

    file_classi_req.write("\end{longtable}\n")
    file_classi_req.write("\egroup\n")
    file_classi_req.write("\end{center}\n")
    file_classi_req.write("% subsection classi_requisiti (end)\n")


def main():
    pass
    print_classi_req()


##############

if __name__ == '__main__':
    main()