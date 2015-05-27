# echo -e "\e[01;32mScript: generazione termini estrappolati dal glossario terminata \e[0m";

default:
	@echo "ATTENZIONE! Nessun comando eseguito"

RR:
	@echo "Script: creazione struttura RR"
	@if [ ! -d consegne/revisione_dei_requisiti ]; then \
		mkdir consegne/revisione_dei_requisiti; \
		mkdir consegne/revisione_dei_requisiti/interni; \
		mkdir consegne/revisione_dei_requisiti/esterni; \
		echo -e "\x1B[01;32m Script: generazione struttura RR completata \x1B[0m"; \
		echo "Script: generazione termini estrappolati dal glossario iniziata"; \
		cd script && make glossterm && cd .. ; \
		echo -e "\x1B[01;32m Script: generazione termini estrappolati dal glossario terminata \x1B[0m"; \
		echo "Script: generazione documenti con comando \gloss{} iniziata"; \
		cd documenti && make gloss && cd .. ; \
		echo "Script: compilazione documenti per RR iniziata"; \
		bash script/consegne/compile_doc.sh; \
		echo -e "\x1B[01;32m Script: compilazione documenti per RR terminata \x1B[0m"; \
		bash script/consegne/copy_doc.sh "RR"; \
		@echo -e "\x1B[01;32m Script: compia documenti dentro consegne/revisione_dei_requisiti terminata \x1B[0m"; \
	else \
		echo -e "\x1B[01;31m Cartella già presente. Non serve creare una nuova struttura per la RR! \x1B[0m"; \
	fi

RP:
	@echo "Script: creazione struttura RP"
	@if [ ! -d consegne/revisione_di_progettazione ]; then \
		mkdir consegne/revisione_di_progettazione; \
		mkdir consegne/revisione_di_progettazione/interni; \
		mkdir consegne/revisione_di_progettazione/esterni; \
		echo -e "\x1B[01;32m Script: generazione struttura RP completata \x1B[0m"; \
		echo "Script: generazione termini estrappolati dal glossario iniziata"; \
		cd script && make glossterm && cd .. ; \
		echo -e "\x1B[01;32m Script: generazione termini estrappolati dal glossario terminata \x1B[0m"; \
		echo "Script: generazione documenti con comando \gloss{} iniziata"; \
		cd documenti && make gloss && cd .. ; \
		echo "Script: compilazione documenti per RP iniziata"; \
		bash script/consegne/compile_doc.sh; \
		echo -e "\x1B[01;32m Script: compilazione documenti per RP terminata \x1B[0m"; \
		bash script/consegne/copy_doc.sh "RP"; \
		echo -e "\x1B[01;32m Script: compia documenti dentro consegne/revisione_di_progettazione terminata \x1B[0m"; \
	else \
		echo -e "\x1B[01;31m Cartella già presente. Non serve creare una nuova struttura per la RP! \x1B[0m"; \
	fi

RQ:
	@echo "Script: creazione struttura RQ"
	@if [ ! -d consegne/revisione_di_qualifica ]; then \
		mkdir consegne/revisione_di_qualifica; \
		mkdir consegne/revisione_di_qualifica/interni; \
		mkdir consegne/revisione_di_qualifica/esterni; \
		echo -e "\x1B[01;32m Script: generazione struttura RQ completata \x1B[0m"; \
		echo "Script: generazione termini estrappolati dal glossario iniziata"; \
		cd script && make glossterm && cd .. ; \
		echo -e "\x1B[01;32m Script: generazione termini estrappolati dal glossario terminata \x1B[0m"; \
		echo "Script: generazione documenti con comando \gloss{} iniziata"; \
		cd documenti && make gloss && cd .. ; \
		echo "Script: compilazione documenti per RQ iniziata"; \
		bash script/consegne/compile_doc.sh; \
		echo -e "\x1B[01;32m Script: compilazione documenti per RQ terminata \x1B[0m"; \
		bash script/consegne/copy_doc.sh "RQ"; \
		echo -e "\x1B[01;32m Script: compia documenti dentro consegne/revisione_di_qualifica terminata \x1B[0m"; \
	else \
		echo -e "\x1B[01;31m Cartella già presente. Non serve creare una nuova struttura per la RQ! \x1B[0m"; \
	fi

RA:
	@echo "Script: creazione struttura RA"
	@if [ ! -d consegne/revisione_di_accettazione ]; then \
		mkdir consegne/revisione_di_accettazione; \
		mkdir consegne/revisione_di_accettazione/interni; \
		mkdir consegne/revisione_di_accettazione/esterni; \
		echo -e "\x1B[01;32m Script: generazione struttura RA completata \x1B[0m"; \
		echo "Script: generazione termini estrappolati dal glossario iniziata"; \
		cd script && make glossterm && cd .. ; \
		echo -e "\x1B[01;32m Script: generazione termini estrappolati dal glossario terminata \x1B[0m"; \
		echo "Script: generazione documenti con comando \gloss{} iniziata"; \
		cd documenti && make gloss && cd .. ; \
		echo "Script: compilazione documenti per RA iniziata"; \
		bash script/consegne/compile_doc.sh; \
		echo -e "\x1B[01;32m Script: compilazione documenti per RA terminata \x1B[0m"; \
		bash script/consegne/copy_doc.sh "RA"; \
		echo -e "\x1B[01;32m Script: compia documenti dentro consegne/revisione_di_accettazione terminata \x1B[0m"; \
	else \
		echo -e "\x1B[01;31m Cartella già presente. Non serve creare una nuova struttura per la RA! \x1B[0m"; \
	fi





test:
	@bash script/consegne/copy_doc.sh "RR"; \