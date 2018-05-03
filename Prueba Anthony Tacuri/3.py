def leertxt():
    archi=open('3.txt','r')
    lineas=archi.readlines()
    archi.close()
    return lineas
def grabartxtnumero(cad):
    archi=open('3.1.txt','a')
    archi.write('La conversion de la cadena es: ')
    archi.close()
def creartxt():
    archi=open('3.1.txt','w')
    archi.close()
datos=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','Q','E']
nombre=str(leertxt())


