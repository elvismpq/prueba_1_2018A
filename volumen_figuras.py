import math as m
def funEsfera(rad):
    vol=(4/3)*m.pi*(rad**3)
    return vol
def calculo_volumen_prisma_triangular(area_base, altura):
    volumen=(area_base*altura)/3
    return volumen
def calculo_volumen_cubo(lad):
    volu3=lad**3
    return volu3
while True :
    print('\t\t\tMenu')
    print('Elija una figura para calcular el volumen:')
    print('1. Esfera')
    print('2. Piramide Triangular')
    print('3. Cubo')
    print('4. Salir')
    o=int(input('Ingrese un numero: '))
    if o==1:
        a=float(input('Ingrese el radio(cm):'))
        print('EL volumen del cubo es ',funEsfera(a),'cm cubicos')
    elif o==2:
        area2 = float(input('Ingrese el area de la base del prisma(cm):'))
        altura2 = float(input('Ingrese la altura del prisma(cm):'))
        print('EL volumen del prisma triangular es ',calculo_volumen_prisma_triangular(area2,altura2),'cm cubicos')
    elif (o==3):
        lado3 = float(input('Ingrese el lado del cubo(cm):'))
        print('El volumen del cubo es: ',calculo_volumen_cubo(lado3),'cm cubicos')
    elif o==4:
        print('Ha salido del menu')
        break;
    else:
        print('Opcion incorrecta ingrese nuevamente')








