"""import sqlite3 - importa la libreria que sirve para conectar y trabajar con bases de datos.

# Conectarse a la base de datos (la crea si no existe)
conexion = sqlite3.connect("ejemplo.db")- Nos conectamos al archivo
cursor = conexion.cursor()- cursor es el objeto que se usa para ejecturar comandos dentro de la conexion

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT,
        edad INTEGER
    )
''')
conexion.commit()- guarda-confirma los cambios realizados en la base de datos. Es necesario cada vez q se hace un INSERT, UPDATE O DELETE.

# ---------- FUNCIONES CRUD ----------

# CREATE
def crear_usuario(nombre, email, edad):
    cursor.execute("INSERT INTO usuarios (nombre, email, edad) VALUES (?, ?, ?)", (nombre, email, edad))
    conexion.commit()
    print("Usuario creado.")

# READ
def leer_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    for fila in cursor.fetchall():
        print(fila)

# UPDATE
def actualizar_usuario(id_usuario, nuevo_nombre, nueva_edad):
    cursor.execute("UPDATE usuarios SET nombre = ?, edad = ? WHERE id = ?", (nuevo_nombre, nueva_edad, id_usuario))
    conexion.commit()
    print("Usuario actualizado.")

# DELETE
def borrar_usuario(id_usuario):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    conexion.commit()
    print("Usuario eliminado.")

# ---------- PRUEBA DEL CRUD ----------

crear_usuario("Ana", "ana@gmail.com", 30)
crear_usuario("Juan", "juan@hotmail.com", 25)

print("\nUsuarios actuales:")
leer_usuarios()

actualizar_usuario(1, "Ana Pérez", 31)

print("\nUsuarios después de actualizar:")
leer_usuarios()

borrar_usuario(2)

print("\nUsuarios después de borrar:")
leer_usuarios()

# Cerrar conexión
conexion.close()"""



import sqlite3
conexion= sqlite3.connect("basededatos.db")
cursor=conexion.cursor("basededatos.db")
conexion.execute('''CREATE TABLA IF NOT EXISTS chikes (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nombre TEXT,
                 email TEXT,
                 edad ometes
                 ))

                 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT,
        edad INTEGER
    )