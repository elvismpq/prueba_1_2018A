import math as m
def funEsfera(rad):
    vol=(4/3)*m.pi*(rad**3)
    return vol
while True :
    print('-----------------Menu-----------------')
    print('Elija una figura que desea sacar el volumen:')
    print('1. Esfera')
    print('2.')
    print('3.')
    print('4. Salir')
    o=int(input('Ingrese un numero=============> '))
    if o==1:
        a=float(input('Ingrese el radio(cm):'))
        print('EL volumen del cubo es ',funEsfera(a),' centimetros')
    elif o==2:
        print('')
    elif (o==3):
        print('')
    elif o==4:
        print('Ha salido del menu')
        break;
    else:
        print('Opcion incorrecta ingrese nuevamente')
