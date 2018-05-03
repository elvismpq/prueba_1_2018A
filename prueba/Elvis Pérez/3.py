cod={'t':0,'r':1,'w':2,'a':3,'g':4,'m':5,'y':6,'f':7,'p':8,'d':9,'x':10,'b':11,'n':12,'j':13,'z':14,'s':15,'q':16,'v':17,'h':18,'l':19,'c':20,'k':21,'e':22}
abr=open('3.txt','r')
men=abr.readline()
abr.close()
print('Mensaje no codificado:\n',men)
new=open('3.2.txt','w')
for e in men:
    if (e in cod):
        new.write(str(cod[e]))
    else:
        new.write(e)
new.close()
leer=open('3.2.txt','r')
print('Mensaje codificado:\n',leer.readline())
leer.close()