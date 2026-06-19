import sqlite3
import os

from northgate.constants import DB_PATH
from northgate.logger import logger


def init_database():
    # Initialize the SQLite database and create the sites table if it doesn't exist
    logger.info("Initializing the database...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS migrations (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            applied_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    run_migrations()

def run_migrations():
    # Get migrations done
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Get migrations done
        cursor.execute('''
            SELECT * FROM migrations
        ''')
        conn.commit()
        output = cursor.fetchall()
        runned_migrations = [row[1] for row in output]
        logger.debug("Migrations applied: {}".format(runned_migrations))

        # Read all .sql in migrations folder
        migrations_folder = os.path.join(os.path.dirname(__file__), 'migrations')
        for filename in os.listdir(migrations_folder):
            if filename.endswith('.sql'):
                migration_name = filename
                if migration_name not in runned_migrations:
                    with open(os.path.join(migrations_folder, filename), 'r') as f:
                        sql = f.read()
                        cursor.executescript(sql)
                        cursor.execute('''
                            INSERT INTO migrations (name, applied_at)
                            VALUES (?, datetime('now'))
                        ''', (migration_name,))
                        conn.commit()
                        logger.info("Applied migration: {}".format(migration_name))
                else:
                    logger.debug("Migration already applied: {}".format(migration_name))
