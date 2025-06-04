# Joaquin01Parcial2
ParcialProgramacion2año
Crear funciones que permitan ejecutar un CRUD correctamente para ello debera crear una base de datos con los siguientes datos:
Nombre DB:parcial
Tabla:productos
Campos:
codigo:int,PK
detalle:Text
stock:Int
precio_costo:real
Crear 1 archivo llamado consultar.py
Dentro del archivo debera crear 3 funciones:conectar,alter_table y search_table
alter_table y serch_table recibiran 2 parametros sql y datos
1 def conetar():
2 def alter_table(sql,datos):
3 def search_table(sql,datos):
Dentro de conetar crear la conexion a la base de datos y devolver la conexion.
Dentro de alter_table debera crear un codigo que le permita al usuario guardar, modificar o eliminar usando solo esa funcion.
La funcion alter_table debera devolver un mensaje distinto por cada accion.
si guardo:"Guardado Exitosamente"
si modifico:"Modificado correctamente"
si elimino:"Eliminado correctamente"
Dentro de lafuncion search_table debera crear un codigo que busque en la base de datos y devuelva los datos encontrados.
Entregar un archivo zip con su nombre y apellido, dentro del archivo comprimido un archivo
que se llame consultas.py.
Ejemplo: ignacioquiroga.zip y dentro consultas.py
