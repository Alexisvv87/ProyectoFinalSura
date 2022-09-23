import pandas as pd

tablaSiembras=pd.read_csv('./Siembras.csv')

#imprime la tabla los primeros registros
#print(tablaEmpleados)
#imprime la tabla todos los registros
#print(tablaEmpleados.to_string())

#quiero tener todos los datos de los analistas 1  
#tablaAnalista1=tablaEmpleados[tablaEmpleados["cargo"]=="analista1"]
#print(tablaAnalista1)

#si quiero solo los 50 primeros le agrego.head(50)

#tablaAnalista1=tablaEmpleados[tablaEmpleados["cargo"]=="analista1"].head(50)
#Exportar la tabla ya creada a un archivo de html
#archivoHTML=tablaAnalista1.to_html()
#crear el archivo y que abra con permisos de escritura se le coloca la "w"
#archivoTEXTO=open("Datosanalistas1.html","w") #abrir el archivo de texto 
#archivoTEXTO.write(archivoHTML) #agregar el archivo de texto el archivo que creamos
#archivoTEXTO.close() #cerrar el archivo de texto 
#tabla analista 2 

#tablaAnalista2=tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)
#Exportar la tabla ya creada a un archivo de html
#archivoHTML=tablaAnalista2.to_html()
#crear el archivo y que abra con permisos de escritura se le coloca la "w"
#archivoTEXTO=open("Datosanalistas2.html","w") #abrir el archivo de texto 
#archivoTEXTO.write(archivoHTML) #agregar el archivo de texto el archivo que creamos
#archivoTEXTO.close() #cerrar el archivo de texto 

tablaDatosxMunicipio=tablaSiembras[(tablaSiembras ['Ciudad'] =="Andes") | (tablaSiembras ['Ciudad'] =="Barbosa") | (tablaSiembras ['Ciudad'] =="Caldas") | (tablaSiembras ['Ciudad'] =="Tamesis")| (tablaSiembras ['Ciudad'] =="Yarumal")]

archivoHTML=tablaDatosxMunicipio.to_html()
archivoTEXTO=open("Datosxmunicipio.html","w")
archivoTEXTO.write(archivoHTML) 
archivoTEXTO.close() 






