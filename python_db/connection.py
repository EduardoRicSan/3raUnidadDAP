import psycopg2
from config import config
"""Connect to Postgresql Database
Programmer: Jesús Eduardo Rico Sandoval"""

def connect():
    """Connect to the Postgresql Database Server"""
    conn = None

    try:
        params = config()

        print('Connecting to the Postgresql database...')
        conn = psycopg2.connect(**params)

        #Create cursor
        cursor = conn.cursor()

        print('Postgresql database version: ')
        cursor.execute('SELECT version()')

        #Display the Postgresql Database Server version
        db_version = cursor.fetchone()
        print(db_version)

        #close the communication with Postgresql
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()