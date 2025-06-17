import sqlite3
import random

conexion = sqlite3.connect('dDBingo.db')
cursor = conexion.cursor()

# Crear la tabla con la columna correcta

N_azar=random.randint(1,100)


cursor.execute("INSERT INTO Bingo (N) VALUES (?)",(N_azar,))
conexion.commit()

print(f' Numero generado:{N_azar}')
cursor.execute("SELECT * FROM Bingo")
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)


conexion.close()
