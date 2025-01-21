import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# Paramètres de connexion.
username = "MimiO"  # Update to your MySQL Workbench username
password = "Iluvme199185!"  # Replace with your actual password
host = "localhost"
port = 3306
database = "my_dbt_db"

# Connexion à la base de données.
DATABASE_URI = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(DATABASE_URI)

# Créer la base de données si elle n'existe pas.
if not database_exists(engine.url):
    create_database(engine.url)

# Importer les fichiers CSV dans des tables.
liste_tables = ["customers", "items", "orders", "products", "stores", "supplies"]
for table in liste_tables:
    csv_url = f"https://raw.githubusercontent.com/dsteddy/jaffle_shop_data/main/raw_{table}.csv"
    df = pd.read_csv(csv_url)
    df.to_sql(f"raw_{table}", engine, if_exists="replace", index=False)
print("Base de données et tables créées avec succès !")
