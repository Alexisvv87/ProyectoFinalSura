from statistics import median
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


#Datos por municipio:
#-Andes
#-Barbosa
#-Caldas
#-Támesis
#-Yarumal
#tablaDatosxMunicipio=tablaSiembras[(
#  | (tablaSiembras ['Ciudad'] =="Barbosa") | (tablaSiembras ['Ciudad'] =="Caldas") | (tablaSiembras ['Ciudad'] =="Tamesis")| (tablaSiembras ['Ciudad'] =="Yarumal")]
#archivoHTML=tablaDatosxMunicipio.to_html()
#archivoTEXTO=open("Datosxmunicipio.html","w",encoding="utf-8")
#archivoTEXTO.write(archivoHTML) 
#archivoTEXTO.close() 

#Los datos de MEDELLIN ordenados de mayor a menor número de arboles
#tablaDatos_Medellin=tablaSiembras[(tablaSiembras ['Ciudad'] =="Medellín")]
#tablaDatos_Medellin=tablaDatos_Medellin.sort_values(by="Arboles")
#archivoHTML=tablaDatos_Medellin.to_html()
#archivoTEXTO=open("ArbolesMedellin.html","w",encoding="utf-8")
#archivoTEXTO.write(archivoHTML) 
#archivoTEXTO.close() 

#Los datos de CAUCASIA incluyendo el número de hectáreas sembradas
#tablaDatos_Caucasia=tablaSiembras[(tablaSiembras ['Ciudad'] =="Caucasia")]
#archivoHTML=tablaDatos_Caucasia.to_html()
#archivoTEXTO=open("Datos_Caucasia.html","w",encoding="utf-8")
#archivoTEXTO.write(archivoHTML) 
#archivoTEXTO.close() 

# Los datos de Santa Fe de Antioquia donde se tengan siembras de >250 arboles
#tablaDatos_Santafe=tablaSiembras[(tablaSiembras ['Ciudad'] =="Santa Fe de Antioquia") & (tablaSiembras ['Arboles'] > 250)]
#archivoHTML=tablaDatos_Santafe.to_html()
#archivoTEXTO=open("Datos_Santafe.html","w",encoding="utf-8")
#archivoTEXTO.write(archivoHTML) 
#archivoTEXTO.close() 

#Los datos de las veredas Rio Arriba y la Salazar de Belmira

#tablaDatos_Veredad_Rio=tablaSiembras[(tablaSiembras ['Vereda'] =="Rio Arriba")|(tablaSiembras ['Vereda'] =="La Salazar")]
#archivoHTML=tablaDatos_Veredad_Rio.to_html()
#archivoTEXTO=open("Datos_veredas_Rio.html","w",encoding="utf-8")
#archivoTEXTO.write(archivoHTML) 
#archivoTEXTO.close() 

#Los datos de la veredas Quitasol de BELLO ordenados de menor a mayor y el promedio de arboles sembrados en esta vereda
tablaDatos_Bello=tablaSiembras[(tablaSiembras ['Ciudad'] =="Bello") & (tablaSiembras ['Vereda'] =="Quitasol")]
tablaDatos_Bello = tablaDatos_Bello.sort_values (by="Arboles")
tablaDatos_Bello=tablaDatos_Bello.sort_values(median="Arboles")
print(tablaDatos_Bello)
#archivoHTML=tablaDatos_Bello.to_html()
#archivoTEXTO=open("Datos_Bello.html","w",encoding="utf-8")
#archivoTEXTO.write(archivoHTML) 
#archivoTEXTO.close() 



#Todos los datos de CARAMANTA

#tablaDatos_caramanta=tablaSiembras[(tablaSiembras ['Ciudad'] =="Caramanta")]
#archivoHTML=tablaDatos_caramanta.to_html()
#archivoTEXTO=open("Datos_Caramanta.html","w",encoding="utf-8")
#archivoTEXTO.write(archivoHTML) 
#archivoTEXTO.close() 









