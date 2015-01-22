#!/bin/bash

doc="documenti_glossario"
# path da escludere
tpl="documenti_glossario/template"
tpl_doc="documenti_glossario/template_document"
lettera="documenti_glossario/lettera_di_presentazione"

for dir in $(find ${doc} -mindepth 1 -maxdepth 1 -type d -not \( -path ${tpl} -o -path ${tpl_doc} \)) ; do

    if [ ${dir} != ${tpl} -o ${dir} != ${tpl_doc} ]; then
        cd ${dir} && make compilenoopen;
        cd ../..;
        # echo ${dir}
    fi

done