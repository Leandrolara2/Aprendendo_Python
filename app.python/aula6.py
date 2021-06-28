conjunto = {1, 2, 3, 4}
#adicionar um conjunto
conjunto.add(5)
#descartar um número do conjunto
conjunto.discard(2)
print(conjunto)

#unir dois conjuntos
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('uniao: {}' .format(conjunto_uniao))

#interceccao dos conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecçao: {}' .format(conjunto_interseccao))

#diferença dos conjuntos
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}' .format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}' .format(conjunto_diferenca2))

# Diferença simetrica tudo que nao tem nos dois.
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}' .format(conjunto_diff_simetrica))

# subconjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset1 = conjunto_a.issubset(conjunto_b)
conjunto_subset2 = conjunto_b.issubset(conjunto_a)
print('A é subconjunto de B: {}'.format(conjunto_subset1))
print('B é subconjunto de A: {}'.format(conjunto_subset2))

#superconjunto
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}' .format(conjunto_superset))

#tirar a duplicidade e transforma em confunto
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

conjunto_a = {1, 1, 3, 4, 5}
conjunto_b = {1, 3, 6}
conjunto_a.add(6)
conjunto_a.remove(1)
resultado = list(conjunto_a.intersection(conjunto_b))
print(resultado)