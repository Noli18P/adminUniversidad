import sqlite3

conection = sqlite3.connect('UNIVERSIDAD')

pointer = conection.cursor()

#pointer.execute("CREATE TABLE ESTUDIANTES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ESTUDIANTE VARCHAR(50), EDAD_ESTUDIANTE INTEGER, ESPAÑOL INTEGER, MATEMATICAS INTEGER, CIENCIAS )")

alumnos = [
        ("MARTIN MARTINEZ", 19, 10,10,10),
        ("JOLETTE PEREZ", 20,8,6,10),
        ("MARIA TORRES", 22, 9,9,9),
        ("EDUARDO ENRIQUEZ", 21, 10, 8, 6),
        ("OLIVIA MARTINEZ", 21, 10, 10, 8)
        ]

pointer.executemany("INSERT INTO ESTUDIANTES VALUES(NULL,?,?,?,?,?)", alumnos)

conection.commit()


conection.close()
