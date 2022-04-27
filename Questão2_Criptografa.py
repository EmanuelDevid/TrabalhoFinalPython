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
