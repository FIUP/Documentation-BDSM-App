#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess

doc_real_path = "../documenti"
doc_path = "../documenti_glossario"
term_maiusc_path = "../script/glossario/glossario_maiusc.txt"
term_min_path = "../script/glossario/glossario_min.txt"

# salvo il contenuto della cartella documenti_gloss
doc_file_list = os.listdir(doc_path)
term_maiusc_file = ""

# prelevo dalla lista solo le cartelle su sulla quale devo effettuare le sostituzioni
docs_dir_list = [d for d in doc_file_list if os.path.isdir(os.path.join(doc_path, d)) and d != "glossario" and
                 d != "template" and d != "template_document" and d != "lettera_di_presentazione"]

# itero sulle cartelle dei documenti sui quali mi interessa fare le sostituzioni
for doc_dir in docs_dir_list:

    content_path = doc_path + "/" + doc_dir + "/" + "content"
    content_static_path = doc_real_path + "/" + doc_dir + "/" + "content"

    # mi prelevo la lista di tutti i file .tex contenuti dentro la cartella del documento che sto esaminando
    # nell'iterazione corrente
    content_list = os.listdir(content_path)
    final_content_list = []
    final_content_list.extend(content_list)

    for content in content_list:
        content_file_path = content_path + "/" + content

        if os.path.isdir(content_file_path):
            final_content_list.remove(content)
            contents_subdir = os.listdir(content_file_path)
            # print contents_subdir
            for content_subdir in contents_subdir:
                print content + "/" + content_subdir
                final_content_list.append(content + "/" + content_subdir)

    # itero su tutti i file .tex contenuti dentro
    for content in final_content_list:
        term_maiusc_file = open(term_maiusc_path, "r")
        term_min_file = open(term_min_path, "r")

        # mi salvo tutte le righe del file in una lista togliendoli il carattere di ritorno a capo
        lines_maiusc_term = [line.strip() for line in term_maiusc_file]
        lines_min_term = [line.strip() for line in term_min_file]

        content_file_path = content_path + "/" + content

        print "Inserisco comando \gloss{} in: " + doc_dir + "/" + content

        # TERMINI MAIUSCOLI
        for line_term in lines_maiusc_term:
            if line_term != "C++":
                # rimpiazzo gli spazi con il simbolo per lo spazio nelle espressioni regolari
                line_new = line_term.replace(" ", "\s")
                #  -> esattamente la parola contenente dentro line_new e nessun altro patter
                line_new = "\\b" + line_new + "\\b"
                term_maiusc_cmd = ["perl", "-i", "-p", "-e", "s/" + line_new + "/" + line_term + "\\\gloss{}/ "
                                   + "if !(m/\\\section/ || m/\\\subsection/"
                                   + " || m/\\\subsubsection/ || m/\\\caption/ || m/\\\includegraphics/"
                                   + " || m/\\\label/ || m/\\\hyperref/ || m/\\\url/ || m/\\\paragraph/"
                                   + " || m/\\\subparagraph/ || m/\\\[r]ef/ || m/\\\[b]egin/ || m/\\\input/ )",
                                   content_file_path]

                subprocess.call(term_maiusc_cmd)

        term_maiusc_file.close()

        # TERMINI MINUSCOLI
        for line_term in lines_min_term:
            if line_term != "c++" or line_term != "view":
                line_new = line_term.replace(" ", "\s")
                line_new = "\\b" + line_new + "\\b"
                term_min_cmd = ["perl", "-i", "-p", "-e", "s/" + line_new + "/" + line_term + "\\\gloss{}/ "
                                + "if !(m/\\\section/ || m/\\\subsection/"
                                + " || m/\\\subsubsection/ || m/\\\caption/ || m/\\\includegraphics/"
                                + " || m/\\\label/ || m/\\\hyperref/ || m/\\\url/ || m/\\\paragraph/"
                                + " || m/\\\subparagraph/ || m/\\\[r]ef/ || m/\\\[b]egin/ || m/\\\input/ )",
                                content_file_path]

                subprocess.call(term_min_cmd)

        term_min_file.close()

sys.exit(0)