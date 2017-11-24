import psycopg2
from config import config
"""Updating information of database
Programmer: Jesús Eduardo Rico Sandoval"""
def update_vendor(vendor_id, vendor_name):
    """Update vendor name based on the vendor id"""
    sql = """UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s """
    try:
        connection = None
        # Variable for load the rows
        updated_rows = 0

        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        cursor.execute(sql, (vendor_name, vendor_id))
        updated_rows = cursor.rowcount
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return updated_rows

if __name__ == '__main__':
    update_vendor(2, '3M Corp.')

