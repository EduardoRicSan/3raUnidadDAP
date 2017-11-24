import psycopg2
from config import config

"""This class allows to insert an image to Posgresql Database 
Programmer: Jesús Eduardo Rico Sandoval"""

def write_blob(part_id, path_to_file, file_extension):
    """ insert a BLOB into a table """
    connection = None
    try:
        # read data from a picture
        drawing = open(path_to_file, 'rb').read()
        # read database configuration
        params = config()
        # connect to the PostgresQL database
        connection = psycopg2.connect(**params)
        # create a new cursor object
        cursor = connection.cursor()
        # execute the INSERT statement
        cursor.execute("INSERT INTO part_drawings(part_id,file_extension,drawing_data) " +
                    "VALUES(%s,%s,%s)",
                    (part_id, file_extension, psycopg2.Binary(drawing)))
        # commit the changes to the database
        connection.commit()
        # close the communication with the PostgresQL database
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    write_blob(1, 'images/goku1.png', 'png')
    write_blob(2, 'images/goku2.jpg', 'jpg')