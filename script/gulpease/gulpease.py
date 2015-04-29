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
# 0.0.2     2015-04-29  Tesser Paolo    aggiunta documentazione a classe e metodi
# -----------------------------------------------------------------------
#
#
__author__ = 'ptesser'


class Gulpease():
    """This class do the computation of Gulpease Index.

    Attributes:
        __num_sentence_int: an int value that indicate the number of sentence in the document.
       __num_letters_int: an integer value that indicate the number of letters in the document.
       __num_words_int: an integer value that indicate the number of words in the document.
    """

    def __init__(self):
        """Init Gulpease Class with blah."""
        self.__num_sentence_int = 0
        self.__num_letters_int = 0
        self.__num_words_int = 0

    def get_num_sentence(self):
        """Return the num of sentence in a document
        Returns:
            A int that corresponding of the number of sentence in a document
        """
        return self.__num_sentence_int

    def get_num_letters(self):
        """Return the num of letters in a document
        Returns:
            A int that corresponding of the number of letters in a document
        """
        return self.__num_letters_int

    def get_num_words(self):
        """Return the num of words in a document
        Returns:
            A int that corresponding of the number of words in a document
        """
        return self.__num_words_int

    def check_gulpease(self, pre_path_str, files_list):
        """This method calculate the value of the gulpease index from a list of files
        Args:
            pre_path_str: A string TODO
            files_list: A list of TODO

        Returns:
            A int that corresponding of the number of sentence in a document

        Raises:
            ZeroDivisionError: An error occurred if
        """
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