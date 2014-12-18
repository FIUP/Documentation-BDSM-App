# -*- coding: utf-8 -*-

# Script di analisi lessicografica basato sulla probabilità di Matt Alcock e modificato da M. Roetta
#
# Come funziona: dato un file "corpus.txt" contenente tutte le parole corrette
# queste vengono contate e le piu frequenti saranno quelle più gettonate nella correzione.
# lo script ritorna la parola più corretta rispetto a quella errata trovata nel testo.
# un buon risultato (80-90% correttezza) richiede circa 1'000'000 di parole
# prese ad esempio da ebook del proghetto Gutenberg.

import re, collections, sys, getopt

def words(text):
    return re.findall('[a-z]+', text.lower())

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(words(file('corpus.txt').read()))
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
    s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in s if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b)>1]
    replaces = [a + c + b[1:] for a, b in s for c in alphabet if b]
    inserts = [a + c + b for a, b in s for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words):
    return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

# Processo un file
# Parte da modificare per scopi vari. Usare correct(parola) per usare il dizionario

# Main da cui "Iniziare" il programma
def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'spellcheck.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile>'
            sys.exit(2)
        elif opt in ("-i", "--ifile"):
            inputfile = arg

    if inputfile == '':
        print 'Non hai specificato un file di input!'
        print 'spellcheck.py -i <inputfile>'
        sys.exit(2)

    # OK, arrivato qui ho degli input validi 
    print 'Input file is ', inputfile

    # Processo il documento
    out_file = open("analisi.log","w")

    for line in words(file(inputfile).read()):
        c = correct(line)
        if c!=line:
            out_file.write("Forse intendevi: "+c)

    # Ok, chiudo
    print "Ho finito!"
    out_file.close()

if __name__ == "__main__":
   main(sys.argv[1:])
