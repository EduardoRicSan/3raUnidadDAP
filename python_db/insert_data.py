import psycopg2
from config import config
"""The class that inserts values to the table vendors of the Database
Programmer: Jesús Eduardo Rico Sandoval"""
def insert_vendors(vendor_name):
    """Insert a new vendor intro the vendors table"""
    sql = """INSERT INTO vendors(vendor_name) 
             VALUES(%s) RETURNING vendor_id;"""
    connection = None
    vendor_id = None
    try:
        #Read database configuration
        params = config()
        #Connect to the PostgreSQL database}
        connection = psycopg2.connect(**params)
        # create a new cursor
        cursor = connection.cursor()
        #execute the INSERT statement
        cursor.execute(sql,(vendor_name,))
        #get the generated id back
        vendor_id = cursor.fetchone()[0]
        #commit the changes to the database
        connection.commit()
        #close the communication with the database
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return vendor_id


def insert_vendor_list(vendor_list):
    """Insert multiple vendors into the vendor table"""
    sql = """INSERT INTO vendors(vendor_name) VALUES(%s) """
    connection = None
    try:
        # Read database configuration
        params = config()
        # Connect to the PostgreSQL database}
        connection = psycopg2.connect(**params)
        # create a new cursor
        cursor = connection.cursor()
        # execute the INSERT statement
        cursor.executemany(sql, vendor_list)
        # commit the changes to the database
        connection.commit()
        # close the communication with the database
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()





if __name__ == '__main__':
   #Insert a vendor
   #Insert one vendor =  print(insert_vendors('3M Co.'))
   #Insert multiple vendors
   insert_vendor_list([('AKM Semiconductor Inc.',),
                       ('Asahi Glass co Ltd.',),
                       ('Daikin Industries Ltd.',),
                       ('Dynacast Internacional Inc.',),
                       ('Foster Electric Co. Ltd.',),
                       ('Murata Manufacturing Co. Ltd.',)])



