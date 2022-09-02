from mysql.connector import connect, Error
from time import sleep

sleep(20)

try:
    with connect (
        host="mysql",
        user = "root",
        password = "qwerty",
        database = "cv_db"
    ) as connection:
        show_tables = "SHOW TABLES"
        with connection.cursor() as cursor:
            cursor.execute(show_tables)
            for db in cursor:
                print(db)

except Error as e:
    print(e)
    print("ОШИБКА")

