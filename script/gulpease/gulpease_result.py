#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name: gulpease_result.py
# Author: Tesser Paolo
# Date: 2015-04-29
# Mail: p.tesser921@gmail.com
# Modify
# Version   Date        Author          Description
# =======================================================================
# 0.0.1     2015-04-29  Tesser Paolo    codifica modulo
# -----------------------------------------------------------------------
#
# -----------------------------------------------------------------------
#
#
__author__ = 'ptesser'
import os
from gulpease import Gulpease


if __name__ == '__main__':
    # dichiaro la variabile che ospiterà l'oggetto Gulpease
    gulp = None

    # percorso di dove andare a recuperare i file che voglio leggere
    doc_real_path = "../../documenti"

    # salvo il contenuto della cartella documenti
    doc_file_list = os.listdir(doc_real_path)

    # prelevo dalla lista solo le cartelle su sulla quale devo effettuare le sostituzioni
    docs_dir_list = [d for d in doc_file_list if os.path.isdir(os.path.join(doc_real_path, d)) and d != "glossario" and
                     d != "template" and d != "template_document" and d != "lettera_di_presentazione"]

    # itero sulle cartelle dei documenti sui quali mi interessa fare le sostituzioni
    for doc_dir in docs_dir_list:
        # creo l'oggetto Gulpease che andrò a richiamare per fare il calcolo dei diversi indici
        gulp = Gulpease()

        content_path = doc_real_path + "/" + doc_dir + "/" + "content"

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
                    final_content_list.append(content + "/" + content_subdir)

        # stampo il valore dell'indice calcolato tramite il metodo della classe Gulpease, passandogli tutti i file
        # presenti nella lista dei file contenuti nella dir del documento in questione
        print doc_dir + ": " + gulp.check_gulpease(content_path, final_content_list)