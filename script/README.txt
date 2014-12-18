ISTRUZIONI SCRIPT

=============================================
Configurare correttamente i git hooks.

Struttura e funzionamento:
	- cartella hooks: contiene i git hooks reali. Per farli funzionare ci sono due modi:
		- Copiare questa cartella e posizionarla nel seguente percorso sostituendo quella presente di default:
				doc_BDSM_App/.git/
		- eseguire da questa root il comando 'make hook', che esegue in automatico le operazioni sopra citate.
				
Questi script contengono solo un richiamo a quelli presenti nella cartella che verrà illustrata successivamente. 
Questo passaggio deve essere fatto da ogni membro del gruppo tutte le volte che esegue una clonazione del repository in quanto i file sotto la dir .git/ non sono versionabili e dipendono localmente dalle modifiche che un membro effettua.
Può essere richiesto esplicitamente dall'amministratore che questa operazione venga effettuata nuovamente se sono state fatte aggiunte o modifiche ai richiami degli script interni. 

	- cartella githooks : contiene gli script che vengono collegati a quelli presenti in hooks_to_copy e riposizionati secondo istruzioni precedenti.
Sono gli script veri che andranno ad effettuare i controlli necessari a mantenere conforme la repo.
Questi possono subire versionamento e vengono gestiti dagli amministratori addetti al mantenimento del repository in questione.

=============================================