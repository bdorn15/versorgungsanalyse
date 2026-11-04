import os
import sys

import psycopg
from dotenv import load_dotenv

load_dotenv()

db_name = os.environ["POSTGRES_DB"]
db_user = os.environ["POSTGRES_USER"]
db_password = os.environ["POSTGRES_PASSWORD"]

try:

    with psycopg.connect(
        host="localhost",
        port=5433,
        dbname=db_name,
        user=db_user,
        password=db_password,
        connect_timeout=5,
        ) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version(), postgis_version();")
            row = cur.fetchone()
            print(f"PostgreSQL Version: {row[0]}, PostGIS Version: {row[1]}")
except psycopg.OperationalError as error:
    print(f"Keine Verbindung zur Datenbank: {error}", file=sys.stderr)
    sys.exit(1)   