# 🎓 University ETL Pipeline  
_Inserimento dati da un file.csv nel database MySQL con un solo comando_

## 📌 Overview 
Questa è una **comand-line ETL pipeline** scritta in Python che:

1. Estrae dati da un file CSV in './data/'
2. Trasforma questi dati (pulisce alcuni campi, divide la location, aggiunge metadati come la provenienza)
3. Lo carica all'interno di una MySQL table ('university_rank') cosi che possano essere analizzati 

## 🏁 Quick Start
## *** Passaggi da fare prima di passare a VSCODE ***

### 1.Prerequisites
- Python >= 3.8
Puoi controlarlo con '''bash python --version''' 
- MySQL server (o un container Docker)
Se non vuoi installare MySQL, si può usare il docker Compose che ho aggiunto alla repository (docker-compose.yml).  comando da eseguire => '''docker-compose up'''
- Librerie Python 
Si installa tutto con '''bash pip install -r requirements.txt'''

### 2. Clone / Download 
Questo è il comando per scaricare il progetto 
'''bash  git clone <repo-url> ''' (scarica cartella ETL con tutto dentro)
'''bash  cd ETL ''' (Entra nella cartella e qui si eseguono i comandi successivi es. python main.py , docker compose up , ecc.).


## Ordine con cui eseguire l'ETL

1. Attivare il Virtual Environment 
2. Installare le dipendenze in requirements.txt
3. Avviare il database con Docker Compose (anche se avviare il container MySQL non ha bisogno dell'ambiente virtuale Python dato che gira indipendentemente, si può quindi fare anche prima o dopo i passi 1-2, ma prima di eseguire main.py)
4. Lanciare l'ETL con '''python main.py [nome_file.csv]''' (file deve essere caricato nella dartella data)

## Maggiori informazioni 

Progetto che ha lo scopo di prendere confidenza con l'uso di Git / GitHub / Docker / creazione virtual environment / creazione di una Pipeline ETL  che possa essere eseguita senza apportare modifiche al codice / Inserimento all'interno dei database all'interno di un'eventuale table da usare in seguito per l'analisi. 

## Possibili Miglioramenti della Pipeline

Si potrebbe migliorare aggiungendo una parte di validazione di del file CSV in entrata.

## Contesto del CSV 

Il file .csv che contiene il ranking delle università del 2021. L'obiettivo è inserire questa informazione all'interno del nostro database mysql in maniera che possano essere ricercabili tramite delle Query SQL e che vogliano essere aggiornate ogni anno. Quindi 'anno prossimo vogliama vere un ETL già pronto che ci permette di avere il nuovo ranking e di inserirlo. Ovviamente vogliamo avere lo storico quindi vogliamo mantenere le informazioni del nostro file. 

La colonna descrizione del file .csv non la inseriremo dentor il database, splitteremo la colonna della Location in città e stato. e la colonna delle tasse la tramuteremo in typo numero piuttosto che stringa cosi da poter effettuare anche operazioni con SQL. 


- Prima di eseguire qualunque codice tipo facendo "python main.py" nel terminale bisogna assicurarsi di aver salvato il file. 