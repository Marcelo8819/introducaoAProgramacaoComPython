a = int(input('Primeiro bimestre:'))
if a > 10:
    a = int(input('Você digitou errado. digite novamente o primeiro bimestre:'))
b = int(input('Segundo bimestre:'))
if b > 10:
    b = int(input('Você digitou errado. digite novamente o segundo bimestre:'))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. digite novamente o terceiro bimestre:'))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. digite novamente o quarto bimestre:'))
media = (a + b + c +d ) / 4
print('media: {}'.format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: {}'.format(media))
# else:
#     print('Foi digitado uma nota errada')

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com  segundovalor: '))
# resto_a = a % 2
# restp_b = b % 2
# if resto_a == 0 or restp_b:
#     print('Foi digitado um número par ')
# else:
#     print('nenhum número par foi digitado')

# a = int(input('Primeiro valor:'))
# b = int(input('Segundo valor:'))
# c = int(input('Terceiro valor:'))
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é: {}'.format(c))
# print('Final do programa!')


