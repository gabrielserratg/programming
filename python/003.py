import random
print('\n') #Pular linha

#Lista
print("Dicas de series e filmes: ")
moveis = ["Silicon valley", "Velozes e furiosos", "Brooklyn 99", "Homem aranha"]

escolido = random.choice(moveis)
print("Filme escolido foi : ", escolido)

print('\n') #Pular linha

#isso vai Listar oque esta na lista!!
print("Listar oque esta na lista")
varlista = ["maionese", "chocolate", "feijao", "arroz", "manga"]
for x in varlista:
    print(x)

print('\n') #Pular lista

#Um determinado item até outro determinado item em ordem
print("Listagem!:")
i = 1
while i < 10:     # mostrar todos os numeros que são abaixo de 10
        print(i)
        i += 1
