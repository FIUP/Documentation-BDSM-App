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
from fonti_requisiti import FontiRequisiti


if __name__ == '__main__':
    print "*** Start: script tracciamento requisiti-fonti ***"

    r = RequisitiFonti()
    r.open_doc_req()
    r.take_req()
    r.write_req_fonti()

    print "*** End: script tracciamento requisiti-fonti ***"

    print "*** Start: script tracciamento fonti-requisiti ***"

    f = FontiRequisiti()
    f.add_fonti_req(r.get_list_fonti())
    f.open_doc_fonti()
    f.set_casi_uso()
    f.write_fonti_req()

    print "*** End: script tracciamento fonti-requisiti ***"