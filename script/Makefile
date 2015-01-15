default:
	@echo "ATTENZIONE! Nessun comando eseguito"

hook:
	@rm -r ../.git/hooks
	@echo "Pulizia completata"
	@cp -r hooks ../.git/hooks
	@echo "Copia completata"

glossterm:
	rm glossario/glossario_maiusc.txt
	@python glossario/search_term_gloss.py