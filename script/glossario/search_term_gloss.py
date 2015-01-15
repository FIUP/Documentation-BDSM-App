import sys
import subprocess
import re
import os


gloss_files_path = "../documenti/glossario/content"
gloss_maiusc_write_path = "glossario/glossario_maiusc.txt"

gloss_read_file = ""
gloss_maiusc_write_file = open(gloss_maiusc_write_path, "a")

gloss_re = re.compile(r"\\textbf{(.*):}")

gloss_files_list = os.listdir(gloss_files_path)


for files_name_path in gloss_files_list:
    gloss_file_path = gloss_files_path + "/" + files_name_path
    gloss_read_file = open(gloss_file_path)

    for line_str in gloss_read_file:
        term_list = gloss_re.findall(line_str)

        for term_str in term_list:
            gloss_maiusc_write_file.write(term_str)