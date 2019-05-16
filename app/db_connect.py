from psycopg2 import connect
import psycopg2.extras
#from config import config
from app import config

def connect():
    conn = None
    try:
        params = config.config()
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return cur
        # execute a statement
        #print('PostgreSQL database version:')
        #cur.execute(query)

        # display the PostgreSQL database server version
        #db_version = cur.fetchone()
        #print(db_version)
        #close the communication with the PostgreSQL
        #cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
 
 
if __name__ == '__main__':
	connect()