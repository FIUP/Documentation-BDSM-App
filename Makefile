default:
	@echo "ATTENZIONE! Nessun comando eseguito"

RR:
	@echo "Script: creazione struttura RR"
	@if [ ! -d consegne/revisione_dei_requisiti ]; then \
		mkdir consegne/revisione_dei_requisiti; \
		mkdir consegne/revisione_dei_requisiti/interni; \
		mkdir consegne/revisione_dei_requisiti/esterni; \
		echo "Script: generazione struttura RR completata"; \
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

test:
	@bash script/consegne/copy_doc.sh "RR"; \