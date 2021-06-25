a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print(type(soma))
soma = str(soma)
print(type(soma))

print('Soma:  {}. \nSubtracao {}. \nMultiplicacao {}. \nDivisao {}. \nResto {}'.format(soma, subtracao, multiplicacao, divisao, resto))
print('soma: {soma}. \nSubtracao {subtracao}' .format(subtracao=subtracao, soma=soma))
print('soma: '+ str(soma))
print('subtracao: '+str(subtracao))
print('multicacao: '+ str(int(multiplicacao)))
print('divisao: '+ str(int(divisao)))
print('resto: '+ str(resto))

# x = '1'
# soma2 = int(x) + 1
# print('essa e a soma2: '+ str(soma2))


