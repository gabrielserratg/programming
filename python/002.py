print('\n') #Pular linha

var1 = "Gabriel"
print(len(var1))  #contar a quantidade de letras
print(var1.upper()) #deixar a palavra em maiusculo
print(var1.lower()) #deixar a palavra em minusculo
print(var1.title()) #Deixar a palavra em titulo , primeira letra maiuscula o resto minusculo

print('\n') #Pular linha

#item abaixo ele compara , c você tem 1 ou 3 sodas , c tiver mais que isso , ele vai retorna no soda for you! , caso ao contrario ele vai mostrar you tem!
varn2 = int(input("your soda : "))

def soda(money):
        if money <= varn2:
            return "You tem!"
        else:
                return "no soda for you!"
print(soda(3))
print(soda(1))

print('\n') #Pular linha

