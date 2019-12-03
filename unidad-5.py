import re #libreria de expreciones regulares

path = "orden.java"

try:
    archivo = open(path, 'r')
except:
    print ("El archivo que intentas abrir no existe")
    quit()

texto = " "
for linea in archivo:
         texto += linea
        
print (texto)


patron = re.compile('[A-Za-z]\w*[ ]*[=][ ]*\w+[.]?\d*')
result = re.findall(patron,texto)

print("\n Resultado de busqueda, sentencias de asignación: ", result)

patron2 = re.compile('[A-Za-z]\w*[ ]*[=][ ]*\w+[.]?\d*[ ]*[+-\/\*][ ]*\w+')
result2 = re.findall(patron2,texto)

print("\n Resultado de busqueda, Operaciones aritméticas básicas: ", result2)

patron3 = re.compile('[A-Za-z]\w*[ ]*[<>!=][=][ ]*[A-Za-z0-9]|[A-Za-z]\w*[ ]*[<>][ ]*[A-Za-z0-9]')
result3 = re.findall(patron3,texto)

print("\n Resultado de busqueda, expresiones booleanas básicas:  ", result3)


#patron4 = re.compile('[A-Za-z]{1,}[\d|\s]{1,}\=[\s|\w|\d.\d]{1,}[\s|\S][\|\/|\%|\+|\-][\s|\]\([\w|\d.\d]{1,}[\S|\s][\|\/|\%|\+|\-][\S|\s][\w|\d.\d]{1,}[ \)|\S\)]')
patron4 = re.compile('[A-Za-z][\w]*[ ]*[=][ ]*\w+[.]?\d*[ ]*[+-\/*%][ ]*\([ ]*\w+[.]?[\d]*[ ]*[+-\/*%][ ]*\w+[.]?[\d]*[ ]*\)')
result4 = re.findall(patron4,texto)

print("\n Resultado de busqueda, Formulas más complejas   ", result4)


patron5 = re.compile('if[ ]*\(.+\)|while[ ]*\(.+\)|for[ ]*\(.+\)')
result5 = re.findall(patron5,texto)

print("\n Resultado de busqueda, encabezado de estructuras de control:  ", result5)




