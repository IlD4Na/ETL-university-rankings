import pandas as pd 
import pymysql
from sqlalchemy import create_engine
import os 
from urllib.parse import quote 
import argparse
# -------------------------------------------------------------------------------
# Creazione di CLI argument parsing per il file .csv
# -------------------------------------------------------------------------------


#  Crea il parser
parser = argparse.ArgumentParser(description="ETL: CSV ➜ MySQL")

#  Definisci un argomento posizionale
parser.add_argument("csv_path", help="Relative path to the CSV file (inside ./data)")

#  Parsa gli argomenti passati da terminale
args = parser.parse_args()

csv_abs = os.path.join("data", args.csv_path)      # ./data/<file>
source_label = f"data/{args.csv_path}"             # value for 'Source' column

# ---------------------------
# Load
# ---------------------------


# Read the CSV file
df = pd.read_csv(csv_abs, encoding='utf-8')


# ---------------------------
# Transform
# ---------------------------


# Drop the 'Description' column
df_to_sql = df.drop(columns=['Description'])  

# Split the 'Location' column into 'City' and 'State'
df[['City', 'State']] = df['Location'].str.split(',', expand=True) 

# Drop the original 'Location' column
df_to_sql = df_to_sql.drop(columns=['Location'])  


# Convert 'Tuition and Fees' to numeric
df_to_sql['Tuition and fees'] = df_to_sql['Tuition and fees'].map(lambda x: x.lstrip('$'))

# Convert 'In-state' to numeric, handling NaN values
df_to_sql['In-state'] = df_to_sql['In-state'].map(lambda x: x if pd.isna(x) else x.lstrip('$'))


# Best Practice : Inserire l'informazione da quale sorgente raw arrivano i dati

# Creazione colonna Source dove inseriamo il path del nostro file .csv
df_to_sql['Source'] = source_label


print(df_to_sql.head(15))

# ---------------------------
# Load ➜ MySQL
# ---------------------------

# In alcune pipeline ETL ha senso inserire anche una colonna con la data di esecuzione della pipeline

# Tramite create_engine creiamo una connessione al nostro database MySQL

sqlEngine = create_engine('mysql+pymysql://root:%s@127.0.0.1/university' % quote('Root123'))

dbConnection = sqlEngine.connect() # Andiamo a creare una connessione con il database

df_to_sql.to_sql('university_rank',con=sqlEngine, if_exists='append') 


print('Dati inseriti correttamente nel database!')

print(f"Numero di righe inserite: {len(df_to_sql)} da {source_label}")