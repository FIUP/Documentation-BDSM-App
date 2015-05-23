latex=pdflatex -synctex=1
# aspell=sudo aspell --mode=tex --lang=it check

compile:
	# python ../../script/tracciamento/tracciamento_st.py
	# mv requisiti-componenti-base.tex content/tracciamento/requisiti-componenti.tex
	$(latex) specifica_tecnica.tex && $(latex) specifica_tecnica.tex
	rm -rf *.aux
	rm -rf *.log
	rm -rf *.out
	rm -rf *.toc
	rm -rf *.synctex.gz
	rm -rf *.lof
	rm -rf *.lot
	@echo "*** Apertura file PDF ***"
	@case $(shell uname) in \
		Darwin*) open specifica_tecnica.pdf;; \
		Linux*) specifica_tecnica.pdf;; \
	esac

compilenoopen:
	# python ../../script/tracciamento/tracciamento_st.py
	# mv requisiti-componenti-base.tex content/tracciamento/requisiti-componenti.tex
	$(latex) specifica_tecnica.tex && $(latex) specifica_tecnica.tex
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
