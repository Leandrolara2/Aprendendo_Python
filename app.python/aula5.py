lista = [67, 1, 3, 59, 5, 7]
lista_animal = ['elefante', 'cachorro', 'gato', 'arara']

tupla = (1, 10, 12, 14)
print(tupla)
# Saber quantos itens tem a lista
print(len(tupla))
print(len(lista))

# Converter a lista em tupla
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

# substituir itens na lista
lista_animal[0] = 'Macaco'
print(lista_animal)


#imprimir um item da lista

#ordenar a lista
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
# ordenar de forma reversa. do final para o começo
lista_animal.reverse()
print(lista_animal)
print(lista_animal[0])

#somar os mumeros da lista
soma = 0
for x in lista:
    print(x)
    soma += x
print(soma)
# imprimir todos os itens da lista
for x in lista_animal:
    print(x)
#somar a lista
print(sum(lista))

# buscar o maior valor na lista
print(max(lista))

# para saber o menor valor da lista
# na lista com strings busca o menor valor do alfabeto
print(min(lista))

# saber se já existe um elemento na lista.
if 'gato' in lista_animal:
    print('Existe um gato na lista')
else:
    print('Não existe um gato na lista')

#multiplicar uma lista
nova_lista = lista_animal * 3
print(nova_lista)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)

# incluir um item na lista .append()

a = input('Escreva o nome de um animal: ')

if a in lista_animal:
    print('Existe o animal {}. na lista'.format(a))
else:
    print('Não existe o animal {}. na lista'.format(a))
    lista_animal.append(a)
    print(lista_animal)

# retirar o ultimo item da lista .pop()
# lista_animal.pop()
# print(lista_animal)

# Escolher um item para remover da lista
lista_animal.remove('cachorro')
print(lista_animal)

lista = [3, 5, 7, 10, 11]
resultado = []
for x in lista:
    if x % 2 == 1:
        resultado.append(x)
print(resultado)