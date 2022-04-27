from math import trunc

class Criptografia(object):
    def criptografar(self):
        print('_' * 70)
        n = int(input('Digite o inteiro de quatro dígitos que deseja criptografar: '))

        n1 = trunc(n / 1000)
        n2 = trunc((n % 1000) / 100)
        n3 = trunc(((n % 1000) % 100) / 10)
        n4 = trunc(((n % 1000) % 100) % 10)

        n1_2 = (n1 + 6) % 10
        n2_2 = (n2 + 6) % 10
        n3_2 = (n3 + 6) % 10
        n4_2 = (n4 + 6) % 10

        n_criptografado = n3_2 * 1000 + n4_2 * 100 + n1_2 * 10 + n2_2

        if n_criptografado == 0:
            print('O número criptografado é: 0000')
        elif n_criptografado < 1000:
            print('O número criptografado é: 0{}'.format(n_criptografado))
        else:
            print('O número criptografado é:', n_criptografado)

        print('_' * 70)


class Descriptografia(object):
    def descriptografar(self):
        print('_' * 70)
        n = int(input('Digite o inteiro de quatro dígitos que deseja descriptografar: '))

        n1 = trunc(n / 1000)
        n2 = trunc((n % 1000) / 100)
        n3 = trunc(((n % 1000) % 100) / 10)
        n4 = trunc(((n % 1000) % 100) % 10)

        if n1 <= 5:
            n1_2 = n1 + 4
        else:
            n1_2 = n1 - 6

        if n2 <= 5:
            n2_2 = n2 + 4
        else:
            n2_2 = n2 - 6

        if n3 <= 5:
            n3_2 = n3 + 4
        else:
            n3_2 = n3 - 6

        if n4 <= 5:
            n4_2 = n4 + 4
        else:
            n4_2 = n4 - 6

        n_descriptografado = n3_2 * 1000 + n4_2 * 100 + n1_2 * 10 + n2_2

        if n_descriptografado == 0:
            print('O número descriptografado é: 0000')
        elif n_descriptografado < 1000:
            print('O número descriptografado é: 0{}'.format(n_descriptografado))
        else:
            print('O número descriptografado é:', n_descriptografado)

        print('_' * 70)


def principal():
    while True:
        print('===== PROGRAMA BÁSICO DE CRIPTOGRAFIA E DESCRIPTOGRAFIA =====')
        n = int(input('Digite:\n1 - Criptografar\n2 - Descriptografar\n0 - Sair\n-> '))
        print('=' * 61)

        if n == 1:
            k = Criptografia()
            k.criptografar()
        elif n == 2:
            k = Descriptografia()
            k.descriptografar()
        elif n == 0:
            print('Programa finalizado!')
            break
        else:
            print('Número inválido!')

principal()
