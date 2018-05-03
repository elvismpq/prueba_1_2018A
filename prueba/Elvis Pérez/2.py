doc=open('2.txt','r')
txt=doc.readline()
doc.close()
print('Texto:\n',txt)
a=len(txt)-1
arch=open('2.2.txt','w')
for i in range(a+1):
    arch.write(txt[a-i])
arch.close
arch=open('2.2.txt','r')
txtinv=arch.readline()
arch.close()
print('Texto invertido:\n',txtinv)