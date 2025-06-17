import sqlite3

def conectar():
    conn=sqlite3.connect("parcial.db")
    return conn
    
def alter_table(sql,datos):
    conn=conectar()
    cursor=conn.cursor()
    try:
        cursor.execute(sql,datos)
        conn.commit()
        accion=sql.strip().split()[0].upper()
        if accion=="INSERT":
            return "Guadado Exitosamente"
        elif accion== "UPDATE":
            return "Modificado Exitosamente"
        elif accion== "DELETE":
            return "Eliminado Correctamente"
        else:
            return "Accion desconocida"
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close()

