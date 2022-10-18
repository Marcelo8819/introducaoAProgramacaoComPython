a = int(input('Primeiro bimestre:'))
while a > 10:
    a = int(input('Você digitou errado. digite novamente o primeiro bimestre:'))
b = int(input('Segundo bimestre:'))
while b > 10:
    b = int(input('Você digitou errado. digite novamente o segundo bimestre:'))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. digite novamente o terceiro bimestre:'))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. digite novamente o quarto bimestre:'))
media = (a + b + c +d ) / 4
print('media: {}'.format(media))
# nota = int(input("Digite a nota: "))
# while nota > 10:
#     nota = int(input("Nota inválida. Entre com a nota correta: "))
#     print(nota)
# a = 0
# while a <= 10:
#     print(a)
#     a += 1 # a = a +1

# a = int(input('Entre com um valor: '))
# for num in range(a + 1):
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         #print(x,resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)


# a = int(input('entre com um número: '))
#
# div = 0
# for x in range (1, a+1):
#     resto = a % x
#     print(x,resto)
# if resto == 0:
#     div +=1
#
# if div ==2:
#     prin('número {} é primo'.format(a))
# else:
#     print('número {} não é primo'.format(a))

