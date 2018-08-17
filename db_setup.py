import os

import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

try:
    with conn.cursor() as cursor:
        sql = """CREATE TABLE IF NOT EXISTS crimes (
                id SERIAL NOT NULL,
                latitude NUMERIC(10,6),
                longitude NUMERIC(10,6),
                date DATE,
                category VARCHAR(50),
                description TEXT,
                updated_at TIMESTAMP,
                PRIMARY KEY (id)
            );"""
        cursor.execute(sql)
    conn.commit()
finally:
    conn.close()
