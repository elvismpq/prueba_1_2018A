def leertxtnumero():
    archi=open('1.txt','r')
    linea=archi.readline()
    archi.close()
    return linea
def grabartxtnumero(res1):
    archi=open('1.1.txt','a')
    archi.write('La conversion del numero binario a decimal es: '+res1)
    archi.close()
def creartxt():
    archi=open('1.1.txt','w')
    archi.close()
print('Bienvenido a la calculadora de conversion de un numero binario a decimal')
linea1=leertxtnumero()
lon=len(linea1)
res=0
lon=6
cont=0
while cont<len(linea1):
    res=res+(int(linea1[cont])*(2**(lon-1)))
    lon=lon-1
    cont=cont+1

cad=str(res)
creartxt()
grabartxtnumero(cad)

