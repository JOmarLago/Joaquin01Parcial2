import sqlite3 
def tabla():
    conn=sqlite3.connect("parcial.db")
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS producto(
            codigo INTEGER PRIMARY KEY,
            detalle TEXT,    
            stock INTEGER,
            precio_costo REAL
        )
        ''')
    conn.commit()
    conn.close()

tabla()
