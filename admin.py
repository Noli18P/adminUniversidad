import sqlite3
import sys


conection = sqlite3.connect('UNIVERSIDAD')

pointer = conection.cursor()

#pointer.execute("CREATE TABLE ESTUDIANTES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ESTUDIANTE VARCHAR(50), EDAD_ESTUDIANTE INTEGER, ESPAÑOL INTEGER, MATEMATICAS INTEGER, CIENCIAS INTEGER)")

"""
alumnos = [
        ("MARTIN MARTINEZ", 19, 10,10,10),
        ("JOLETTE PEREZ", 20,8,6,10),
        ("MARIA TORRES", 22, 9,9,9),
        ("EDUARDO ENRIQUEZ", 21, 10, 8, 6),
        ("OLIVIA MARTINEZ", 21, 10, 10, 8)
        ]


pointer.executemany("INSERT INTO ESTUDIANTES VALUES(NULL,?,?,?,?,?)", alumnos)
conection.commit()"""

def registrar_estudiante():
    nombre = input('Ingresa tu nombre: ').upper()
    edad = int(input('Ingresa tu edad: '))
    
    datos = [
            (nombre, edad)
            ]

    pointer.executemany('INSERT INTO ESTUDIANTES VALUES(NULL,?,?,NULL,NULL,NULL)', datos)

    conection.commit()


def actualizar_calificacion():
    print('Puedes actualizar varias calificaciones o solo una!!')
    nombre = input('Ingresa tu nombre: ').upper()
    opcion = int(input('Ingresa la cantidad de calificaciones que quieres actualizar: '))

    if opcion == 1:
        materia = input('Ingresa el nombre de la materia: ')
        calificacion = int(input('Ingresa tu calificacion: '))
        
        if materia == 'español':
            materia = 'ESPAÑOL'
        else:
            materia = materia.upper()

        sql = f"UPDATE ESTUDIANTES SET {materia} = {calificacion} WHERE NOMBRE_ESTUDIANTE='{nombre}'"
        pointer.execute(sql)
        print('Listo!')
        conection.commit()
    elif opcion == 2:
        i = 0
        while i < 2:
            materia = input('Ingresa el nombre de la materia: ').upper()
            calificacion = int(input('Ingresa tu calificacion: '))
            
            if materia == 'español':
                materia = 'ESPAÑOL'
            else:
                materia = materia.upper()

            sql = f"UPDATE ESTUDIANTES SET {materia} = {calificacion} WHERE NOMBRE_ESTUDIANTE='{nombre}'"
            pointer.execute(sql)
            print('Listo!')
            conection.commit()
            i = i + 1
    elif opcion == 3:
        i = 0
        while i < 3:
            materia = input('Ingresa el nombre de la materia: ').upper()
            calificacion = int(input('Ingresa tu calificacion: '))
            
            if materia == 'español':
                materia = 'ESPAÑOL'
            else:
                materia = materia.upper()

            sql = f"UPDATE ESTUDIANTES SET {materia} = {calificacion} WHERE NOMBRE_ESTUDIANTE='{nombre}'"
            pointer.execute(sql)
            print('Listo!')
            conection.commit()
            i = i + 1


def eliminar_estudiante():
    nombre = input('Ingresa tu nombre: ').upper()
    pointer.execute(f"DELETE FROM ESTUDIANTES WHERE NOMBRE_ESTUDIANTE = '{nombre}'")
    print('Estudiante eliminado!')
    conection.commit()


def leer_calificaciones():
    nombre = 

def main():
    print("""
            Seleccione una opcion: 

            1 - Registrar a un nuevo estudiante
            2 - Eliminar a un estudiante
            3 - Actualizar la calificación de un estudiante
            4 - Leer las calificaciones de un estudiante
            5 - Salir

            """)

    opcion = int(input())
    
    if opcion == 1:
        registrar_estudiante()
    elif opcion == 2:
        eliminar_estudiante()
    elif opcion == 3:
        actualizar_calificacion()
    elif opcion == 4:
        pass
    elif opcion == 5:
        sys.exit()
    else:
        print('La opcion ingresada no existe, intentalo otra vez')
        main()


if __name__ == '__main__':
    main()




conection.close()
