#funcion para hacer filtros 
from modulo import crearTabla
from modulo2 import generarHtml


def filtro1():
        tablaMunicipios=crearTabla()
        tablaBarbosa=tablaMunicipios[tablaMunicipios["cuidad"]=="barbosa"]
        generarHtml(tablaBarbosa,"barbosa.html")

        filtro1()

