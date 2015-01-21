latex=pdflatex -synctex=1 -interaction=nonstopmode
# aspell=sudo aspell --mode=tex --lang=it check

compile: 
	$(latex) piano_di_qualifica.tex && $(latex) piano_di_qualifica.tex
	rm -rf *.aux 
	rm -rf *.log
	rm -rf *.out
	rm -rf *.toc 
	rm -rf *.synctex.gz
	rm -rf *.lof
	rm -rf *.lot
	@echo "*** Apertura file PDF ***"
	@case $(shell uname) in \
		Darwin*) open piano_di_qualifica.pdf;; \
		Linux*) piano_di_qualifica.pdf;; \
	esac

compilenoopen:
	$(latex) piano_di_qualifica.tex && $(latex) piano_di_qualifica.tex
	rm -rf *.aux 
	rm -rf *.log
	rm -rf *.out
	rm -rf *.toc 
	rm -rf *.synctex.gz
	rm -rf *.lof
	rm -rf *.lot

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
