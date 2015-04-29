#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Name: gulpease.py
# Author: Tesser Paolo
# Date: 2015-04-29
# Mail: p.tesser921@gmail.com
# Modify
# Version   Date        Author          Description
# =======================================================================
# 0.0.1     2015-04-29  Tesser Paolo    creazione classe
# -----------------------------------------------------------------------
#
# -----------------------------------------------------------------------
#
#
__author__ = 'ptesser'


class Gulpease():

    def __init__(self):
        self.__num_sentence_int = 0
        self.__num_letters_int = 0
        self.__num_words_int = 0
    """
    """
    def get_num_sentence(self):
        return self.__num_sentence_int

    """
    """
    def get_num_letters(self):
        return self.__num_letters_int

    """
    """
    def get_num_words(self):
        return self.__num_words_int

    """
    """
    def check_gulpease(self, pre_path_str, files_list):

        for file_str in files_list:
            path_str = pre_path_str + "/" + file_str
            doc_file = open(path_str, "r")

            lines_list = [line.strip() for line in doc_file]

            for line in lines_list:
                new_line = line.replace("(.*)", "")
                print new_line

        try:
            gulp_index = 89 + ((300 * self.get_num_sentence() - 10 * self.get_num_letters()) / self.get_num_words())
            return str(gulp_index)

        except ZeroDivisionError:
            return "VALUE NOT VALID"