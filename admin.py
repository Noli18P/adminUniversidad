import sqlite3

conection = sqlite3.connect('UNIVERSIDAD')

pointer = conection.cursor()

pointer.execute("CREATE TABLE ESTUDIANTES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ESTUDIANTE VARCHAR(50), EDAD_ESTUDIANTE INTEGER, ESPAÑOL INTEGER, MATEMATICAS INTEGER, CIENCIAS )")

conection.commit()


conection.close()
