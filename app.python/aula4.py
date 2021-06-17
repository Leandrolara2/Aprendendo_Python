a = int(input("Entre com o número: "))

for num in range(a + 1):
    div = 0
    for x in range(1, num + 1):
        resto = num % x
        #print(x, resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(num)





# a = int(input("Entre com o número: "))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não e primo.'.format(a))



# for x in range(89, 101):
#     print(x)