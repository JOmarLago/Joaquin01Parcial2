from Main_parcial import tabla
from consultar import alter_table

# Crear la tabla (resetea todo)
tabla()

# Insertar un producto
sql = "INSERT INTO producto (codigo, detalle, stock, precio_costo) VALUES (?, ?, ?, ?)"
datos = (1, "Destornillador", 50, 1250.75)

resultado = alter_table(sql, datos)
print(resultado)