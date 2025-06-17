import sqlite3
from tkinter import Frame, Tk, Label, Entry, Button, ttk, StringVar, messagebox

# Configuración de la base de datos
def inicializar_db():
    conexion = sqlite3.connect("Previa Programacion.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            trabaja TEXT NOT NULL UNIQUE,
            Horas INTEGER,
            email TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

# Función para cargar alumnos en la tabla
def cargar_datos():
    for fila in tabla.get_children():
        tabla.delete(fila)
    conexion = sqlite3.connect("Previa Programacion.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM alumnos ")
    for alumnos  in cursor.fetchall():
        tabla.insert("", "end", values=alumnos )
    conexion.close()

# Función para agregar un alumno
def agregar_alumnos ():
    nombre = entry_nombre.get()
    trabaja = entry_trabaja.get()
    horas = entry_horas.get()
    email = entry_email.get()

    if not nombre or not trabaja :
        messagebox.showerror("Error", "El nombre y trabajo son obligatorios.")
        return

    conexion = sqlite3.connect("Previa Programacion.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO alumnos (nombre, trabaja, horas, email) VALUES (?, ?, ?,?)", (nombre, trabaja, horas, email))
        conexion.commit()
        messagebox.showinfo("Éxito", "Alumno agregado correctamente.")
        cargar_datos()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El email ya está registrado.")
    finally:
        conexion.close()

# Función para seleccionar un cliente de la tabla
def seleccionar_alumno(event):
    item = tabla.selection()
    if item:
        alumno = tabla.item(item, "values")
        entry_id.set(alumno[0])
        entry_nombre.set(alumno[1])
        entry_trabaja.set(alumno[2])
        entry_horas.set(alumno[3])
        entry_email.set(alumno[4])

# Función para actualizar un cliente
def actualizar_alumnos():
    alumno_id = entry_id.get()
    nombre = entry_nombre.get()
    trabaja = entry_trabaja.get()
    horas = entry_horas.get()
    email = entry_email.get()

    if not alumno_id:
        messagebox.showerror("Error", "No se ha seleccionado un alumno para actualizar.")
        return

    conexion = sqlite3.connect("Previa Programacion.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE alumnos SET nombre = ?, trabaja = ?, horas = ?, email = ? WHERE id = ?", (nombre, trabaja, horas, email, alumno_id))
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Éxito", "Alumno actualizado correctamente.")
    cargar_datos()

# Función para eliminar un alumno
def eliminar_alumnos():
    alumno_id = entry_id.get()
    if not alumno_id:
        messagebox.showerror("Error", "No se ha seleccionado un alumno para eliminar.")
        return

    respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este alumno?")
    if respuesta:
        conexion = sqlite3.connect("Previa Programacion.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM alumnos WHERE id = ?", (alumno_id,))
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
        cargar_datos()

# Configuración de la interfaz de usuario
root = Tk()
# Tamaño y fondo ventana principal
root.geometry("800x600")
root.config(bg="gray18")
root.title("Registro de Alumnos con trabajo")
root.resizable(True,True)
# Titulo
frame1=Frame(root,bg="PaleGreen3",highlightbackground="black",highlightthickness=1)
frame1.pack(side="top",fill="y")
titulo=Label(frame1, text="Registro de alumnos con Empleo", bg="PaleGreen3", font=("Arial", 12, "bold"))
titulo.pack()

# Marco
marco = Frame(root, bg="LightCyan2", highlightbackground="chartreuse4", highlightthickness=4)
marco.pack(fill="y", expand=True, anchor="n", pady=(10, 200))
marco.config(width=800, height=600)
# Menu para cargar datos
frame = Frame(marco, bg="azure",highlightbackground="black",highlightthickness=2)
frame.pack(padx=50, pady=20)
frame.config(width=300, height=100)


# Expansión del grid dentro del frame.


Label(frame, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_id = StringVar()
Entry(frame, textvariable=entry_id, state="readonly").grid(row=0, column=1, padx=(50,0), pady=5)

Label(frame, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_nombre = StringVar()
Entry(frame, textvariable=entry_nombre).grid(row=1, column=1, padx=(50,0), pady=5)

Label(frame, text="Trabaja:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_trabaja = StringVar()
Entry(frame, textvariable=entry_trabaja).grid(row=2, column=1, padx=(50,0), pady=5)

Label(frame, text="Horas/mes:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_horas = StringVar()
Entry(frame, textvariable=entry_horas).grid(row=3, column=1, padx=(50,0), pady=5)

Label(frame, text="Email:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
entry_email = StringVar()
Entry(frame, textvariable=entry_email).grid(row=4, column=1, padx=(50,0), pady=5)


Button(frame, text="Agregar", command=agregar_alumnos).grid(row=5, column=0, padx=10, pady=5)
Button(frame, text="Actualizar", command=actualizar_alumnos).grid(row=5, column=1, padx=0, pady=5)
Button(frame, text="Eliminar", command=eliminar_alumnos).grid(row=5, column=2, padx=10, pady=5)

# Tabla para mostrar los clientes
style=ttk.Style()
style.configure("Treeview", 
                background="#e6f2ff",   
                foreground="black",               
                fieldbackground="#e6f2ff")
style.configure("Treeview.Heading",     
                font=("Arial", 10, "bold"))
 

frame_tabla = Frame(marco, highlightbackground="black", highlightthickness=1)
frame_tabla.pack(side="top", fill="both", expand=True, padx=50, pady=10)

tabla = ttk.Treeview(frame_tabla,columns=("ID", "Nombre", "Trabaja", "Horas", "Email"), show="headings")
tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Trabaja", text="Trabaja")
tabla.heading("Horas", text="Horas/mes")
tabla.heading("Email", text="Email")
tabla.bind("<ButtonRelease-1>", seleccionar_alumno)
tabla.pack(expand=True, fill="both",padx=10, pady=10)

# Ajustar tamaños de las columnas
tabla.column("ID", width=50, anchor="center")
tabla.column("Nombre", width=130, anchor="center")
tabla.column("Trabaja", width=80, anchor="center")
tabla.column("Horas", width=80, anchor="center")
tabla.column("Email", width=130, anchor="center")
# Inicializar base de datos y cargar datos
inicializar_db()
cargar_datos()
# Ejecutar la aplicación
root.mainloop()