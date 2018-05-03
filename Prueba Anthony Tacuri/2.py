def leertxt():
    archi=open('2.txt','r')
    lineas=archi.readline()
    archi.close()
    return lineas
def grabartxtnumero(cad):
    archi=open('2.1.txt','a')
    archi.write('La conversion de la cadena es: '+cad)
    archi.close()
def creartxt():
    archi=open('2.1.txt','w')
    archi.close()
print('Bienvenido al programa de conversion de cadenas de texto')
print('La cadena a convertir es: ', leertxt())
cadena=str(leertxt())
cadena1=cadena.split(" ")
cadena2=cadena1
lon=len(cadena2)-2
con=0
caracter=" "
while con<len(cadena1):
    print(cadena1)
    palabra=cadena1[lon]
    cadena2[con]=palabra
    con=con+1
    lon=lon-1
grabartxtnumero(caracter.join(cadena2))
