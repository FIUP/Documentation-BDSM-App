# echo -e "\e[01;32mScript: generazione termini estrappolati dal glossario terminata \e[0m";

default:
	@echo "ATTENZIONE! Nessun comando eseguito"

RR:
	@echo "Script: creazione struttura RR"
	@if [ ! -d consegne/revisione_dei_requisiti ]; then \
		mkdir consegne/revisione_dei_requisiti; \
		mkdir consegne/revisione_dei_requisiti/interni; \
		mkdir consegne/revisione_dei_requisiti/esterni; \
		echo "Script: generazione struttura RR completata"; \
		echo "Script: generazione termini estrappolati dal glossario iniziata"; \
		cd script && make glossterm && cd .. ; \
		echo "Script: generazione termini estrappolati dal glossario terminata"; \
		echo "Script: generazione documenti con comando \gloss{} iniziata"; \
		cd documenti && make gloss && cd .. ; \
		echo "Script: compilazione documenti per RR iniziata"; \
		bash script/consegne/compile_doc.sh; \
		echo "Script: compilazione documenti per RR terminata"; \
		bash script/consegne/copy_doc.sh "RR"; \
		echo "Script: compia documenti dentro consegne/revisione_dei_requisiti terminata"; \
	else \
		echo "Cartella già presente. Non serve creare una nuova struttura per la RR!"; \
	fi

RP:
	@echo "Script: creazione struttura RP"
	@if [ ! -d consegne/revisione_di_progettazione ]; then \
		mkdir consegne/revisione_di_progettazione; \
		mkdir consegne/revisione_di_progettazione/interni; \
		mkdir consegne/revisione_di_progettazione/esterni; \
		echo "Script: generazione struttura RR completata"; \
		echo "Script: generazione termini estrappolati dal glossario iniziata"; \
		cd script && make glossterm && cd .. ; \
		echo "Script: generazione termini estrappolati dal glossario terminata"; \
		echo "Script: generazione documenti con comando \gloss{} iniziata"; \
		cd documenti && make gloss && cd .. ; \
		echo "Script: compilazione documenti per RP iniziata"; \
		bash script/consegne/compile_doc.sh; \
		echo "Script: compilazione documenti per RP terminata"; \
		bash script/consegne/copy_doc.sh "RP"; \
		echo "Script: compia documenti dentro consegne/revisione_di_progettazione terminata"; \
	else \
		echo "Cartella già presente. Non serve creare una nuova struttura per la RP!"; \
	fi

RQ:
	@echo "Script: creazione struttura RQ"
	@if [ ! -d consegne/revisione_di_qualifica ]; then \
		mkdir consegne/revisione_di_qualifica; \
		mkdir consegne/revisione_di_qualifica/interni; \
		mkdir consegne/revisione_di_qualifica/esterni; \
		echo "Script: generazione struttura RQ completata"; \
		echo "Script: generazione termini estrappolati dal glossario iniziata"; \
		cd script && make glossterm && cd .. ; \
		echo "Script: generazione termini estrappolati dal glossario terminata"; \
		echo "Script: generazione documenti con comando \gloss{} iniziata"; \
		cd documenti && make gloss && cd .. ; \
		echo "Script: compilazione documenti per RQ iniziata"; \
		bash script/consegne/compile_doc.sh; \
		echo "Script: compilazione documenti per RQ terminata"; \
		bash script/consegne/copy_doc.sh "RQ"; \
		echo "Script: compia documenti dentro consegne/revisione_di_qualifica terminata"; \
	else \
		echo "Cartella già presente. Non serve creare una nuova struttura per la RQ!"; \
	fi

RA:
	@echo "Script: creazione struttura RA"
	@if [ ! -d consegne/revisione_di_accettazione ]; then \
		mkdir consegne/revisione_di_accettazione; \
		mkdir consegne/revisione_di_accettazione/interni; \
		mkdir consegne/revisione_di_accettazione/esterni; \
		echo "Script: generazione struttura RA completata"; \
		echo "Script: generazione termini estrappolati dal glossario iniziata"; \
		cd script && make glossterm && cd .. ; \
		echo "Script: generazione termini estrappolati dal glossario terminata"; \
		echo "Script: generazione documenti con comando \gloss{} iniziata"; \
		cd documenti && make gloss && cd .. ; \
		echo "Script: compilazione documenti per RA iniziata"; \
		bash script/consegne/compile_doc.sh; \
		echo "Script: compilazione documenti per RA terminata"; \
		bash script/consegne/copy_doc.sh "RA"; \
		echo "Script: compia documenti dentro consegne/revisione_di_accettazione terminata"; \
	else \
		echo "Cartella già presente. Non serve creare una nuova struttura per la RA!"; \
	fi





test:
	@bash script/consegne/copy_doc.sh "RR"; \