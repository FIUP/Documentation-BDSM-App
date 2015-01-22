#!/bin/bash

INTERNI=("norme_di_progetto" "studio_di_fattibilita" "verbale_interno_2014-11-26" "verbale_interno_2014-12-02");
ESTERNI=("analisi_dei_requisiti" "piano_di_progetto" "piano_di_qualifica" "glossario" "verbale_esterno_2015_01_14")

doc_to_copy="documenti_glossario/"
tpl=${doc_to_copy}"/template"
tpl_doc=${doc_to_copy}"/template_document"
lettera=${doc_to_copy}"/lettera_di_presentazione"

if [ $1 == "RR" ]; then
    revisione="revisione_dei_requisiti";
fi

if [ $1 == "RP" ]; then
    revisione="revisione_di_progettazione";
fi

if [ $1 == "RQ" ]; then
    revisione="revisione_di_qualifica";
fi

if [ $1 == "RA" ]; then
    revisione="revisione_dei_requisiti";
fi

# copio tutti i documenti interni del gruppo nell'apposita sezione
for i in ${INTERNI[@]}; do
    cp ${doc_to_copy}${i}"/"${i}".pdf" "consegne/"${revisione}"/interni/"${i}".pdf";
done

# copio tutti i documenti esterni del gruppo nell'apposita sezione
for i in ${ESTERNI[@]}; do
    cp ${doc_to_copy}${i}"/"${i}".pdf" "consegne/"${revisione}"/esterni/"${i}".pdf";
done

# TO DO lettere di presentazione
cp ${doc_to_copy}"lettera_di_presentazione/lettera_di_presentazione.pdf" "consegne/"${revisione}"/lettera_di_presentazione.pdf";