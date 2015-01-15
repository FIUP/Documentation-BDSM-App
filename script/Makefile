default:
	@echo "ATTENZIONE! Nessun comando eseguito"

hook:
	@echo "Script: installazione/aggiornamento hooks iniziato"
	@rm -r ../.git/hooks
	@echo "Pulizia hooks vecchi completata"
	@cp -r hooks ../.git/hooks
	@echo "Script: installazione/aggiornamento hooks completato"

glossterm:
	rm glossario/glossario_maiusc.txt
	rm glossario/glossario_min.txt
	@echo "Script: estrappolazione termini iniziata"
	@python glossario/search_term_gloss.py
	@echo "Script: estrappolazione termini completata"