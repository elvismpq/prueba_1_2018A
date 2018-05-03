doc=open('1.txt','r')
bi=doc.readline()
doc.close()
numIn=0
a=len(bi)-1
for i in range(a+1):
    numIn=numIn+(int(bi[a-i]))*(2**(i))
print('Transformacion de numeros binarios a decimales')
print('Binario: ',bi,'====> Entero: ',numIn)