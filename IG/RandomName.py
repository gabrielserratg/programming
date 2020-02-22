import random

Filename='/root/Desktop/programming/Python-resultados/firstnames.txt'
File=open(Filename,'r').readlines()
name=random.choice(File)[:-1]
name=name+' '
name=name+random.choice(File)[:-1]
print name
