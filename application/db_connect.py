from psycopg2 import connect
import psycopg2.extras
from application import config

def db_connect(query, parameter =  None):
    conn = None
    try:
        params = config.config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(query, (parameter,))
        row_headers=[desc[0] for desc in cur.description] # automagically get row headers 
        data = cur.fetchall()

        return (data, row_headers)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
         if conn:
            conn.close()
            print("Connection closed")