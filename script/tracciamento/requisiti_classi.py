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
from requisiti_fonti import RequisitiFonti

if __name__ == '__main__':
    print "*** Start: generazione file contenente lista requisiti per tracciamento requisiti-classi"

    r = RequisitiFonti()
    r.open_doc_req()
    r.open_doc_classi()
    r.take_req()
    r.take_req_comp()
    r.write_list_req_for_class()

    print "*** End: generazione file contenente lista requisiti per tracciamento requisiti-classi"