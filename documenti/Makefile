# @ symbol applied before commands prevent the print of the command in the shell view

# You will need to use \ line continuations so that the whole sequence is executed as one shell script, 
# otherwise Make will spawn a new shell for each line.
# That means that anything you read will disappear as soon as its shell exits.

# FUNZIONAMENTO
# 1. prelevo il nome del file che voglio generare
# 2. copio la cartella template_document e la rinomino con il nome inserito
# 3. rinomino i file del tipo nome_del_documento con il nuovo nome
# 4. all'interno del Makefile presente nella dir copiata, sostituisco tutte le occ di nome_del_documento con il nuovo nome
# l'opzione -i '' di sed modifica sul posto il file in input facendo perdere la copia originale

doc:
	@echo "Enter a document name:"
	@read DOC_NAME; \
	cp -r template_document $$DOC_NAME; \
	cd $$DOC_NAME; \
	mv nome_del_documento.tex $$DOC_NAME.tex; \
	rm nome_del_documento.pdf; \
	sed -i '' "s/nome_del_documento/$$DOC_NAME/g" Makefile; \
	echo "Generazione struttura $$DOC_NAME completata"