import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base  

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/f1_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def criar_tabelas():
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas")

def importar_csv(nome_csv, nome_tabela):
    print(f"Importando {nome_csv} para {nome_tabela}...")
    df = pd.read_csv(nome_csv)



    df.to_sql(nome_tabela, con=engine, if_exists='append', index=False)
    print(f"{nome_tabela} importada com sucesso!")

if __name__ == "__main__":
    criar_tabelas()

    arquivos_tabelas = {
        'f1_data/circuits.csv': 'circuits',
        'f1_data/constructors.csv': 'constructors',
        'f1_data/constructor_results.csv': 'constructor_results',
        'f1_data/constructor_standings.csv': 'constructor_standings',
        'f1_data/drivers.csv': 'drivers',
        'f1_data/driver_standings.csv': 'driver_standings',
        'f1_data/lap_times.csv': 'lap_times',
        'f1_data/pit_stops.csv': 'pit_stops',
        'f1_data/qualifying.csv': 'qualifying',
        'f1_data/races.csv': 'races',
        'f1_data/results.csv': 'results',
        'f1_data/seasons.csv': 'seasons',
        'f1_data/sprint_results.csv': 'sprint_results',
        'f1_data/status.csv': 'status',
    }

    for arquivo, tabela in arquivos_tabelas.items():
        importar_csv(arquivo, tabela)
