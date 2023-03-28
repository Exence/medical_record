from psycopg2 import connect, OperationalError
from settings import settings


def get_connection():
    connection = None
    try:
        connection = connect(
            database=settings.db_name,
            user=settings.db_user,
            password=settings.db_password,
            host=settings.db_host,
            port=settings.db_port,
        )
        print("Connection to PostgreSQL DB successful")
        yield connection
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    finally:
        connection.close()

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")