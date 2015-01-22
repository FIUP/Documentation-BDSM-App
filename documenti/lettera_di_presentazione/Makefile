latex=pdflatex -synctex=1 -interaction=nonstopmode
# aspell=sudo aspell --mode=tex --lang=it check

compile: 
	$(latex) lettera_di_presentazione.tex && $(latex) lettera_di_presentazione.tex
	rm -rf *.aux 
	rm -rf *.log
	rm -rf *.out
	rm -rf *.toc 
	rm -rf *.synctex.gz
	rm -rf *.lof
	rm -rf *.lot
	@echo "*** Apertura file PDF ***"
	@case $(shell uname) in \
		Darwin*) open lettera_di_presentazione.pdf;; \
		Linux*) lettera_di_presentazione.pdf;; \
	esac

aspell:
	# $(aspell) Studio_di_Fattibilita.tex
	# cd Doc_to_Modify && $(aspell) History.tex
	# cd content &&  $(aspell) Introduzione.tex
	# cd content &&  $(aspell) Capitolato_1.tex
	# cd content &&  $(aspell) Capitolato_2.tex
	# cd content &&  $(aspell) Capitolato_3.tex
	# cd content &&  $(aspell) Capitolato_4.tex
	# cd content &&  $(aspell) Capitolato_5.tex
	# cd content &&  $(aspell) Considerazioni.tex
clean:
	rm -rf *.aux 
	rm -rf *.log
	rm -rf *.out
	rm -rf *.toc 
	rm -rf *.synctex.gz
	rm -rf *.pdf
	rm -rf *.lof
	rm -rf *.lot
