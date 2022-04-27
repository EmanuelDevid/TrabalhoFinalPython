class NumerosComplexos(object):

    #inicializa um múmero com parte real e imaginária
    def inicializaNumero(self, a, b):
        self.p_real = float(a)
        self.p_imag = float(b)

    #inicializa um número com parte real
    def inicializaReal(self, a):
        self.p_real = float(a)
        self.p_imag = 0.0

    #inicializa um número com as partes real e imaginária iguais 0
    def inicializaZero(self):
        self.p_real = 0.0
        self.p_imag = 0.0

    #imprime um número complexo
    def imprimeNumero(self):
        if self.p_imag < 0:
            num = '{} - {}i'.format(self.p_real, (-1 * self.p_imag))
            print('O número é: ', num)
        elif self.p_imag == 0:
            print('O número é: ', self.p_real)
        else:
            num = '{} + {}i'.format(self.p_real, self.p_imag)
            print('O número é: ', num)

    #recebe como parâmetro as partes real e imaginária de outro número e verifica se são iguais (True) ou não (False)
    def éIgual(self, c, d):
        self.p_real2 = float(c)
        self.p_imag2 = float(d)

        if self.p_real == self.p_real2 and self.p_imag == self.p_imag2:
            return True
        else:
            return False

    #inicializa outro número, soma com o já inicializado e mostra o resultado na tela
    def soma(self):
        print('-' * 60)
        c = float(input('Digite a parte real do outro número complexo: '))
        d = float(input('Digite a parte imaginária do outro número complexo: '))
        n2 = NumerosComplexos()
        n2.inicializaNumero(c, d)
        n2.p_real2 = c
        n2.p_imag2 = d

        if self.p_imag < 0:
            num1 = '{} - {}i'.format(self.p_real, -1 * self.p_imag)
        elif self.p_imag == 0:
            num1 = self.p_real
        else:
            num1 = '{} + {}i'.format(self.p_real, self.p_imag)

        if n2.p_imag2 < 0:
            num2 = '{} - {}i'.format(n2.p_real2, -1 * n2.p_imag2)
        elif n2.p_imag2 == 0:
            num2 = n2.p_real2
        else:
            num2 = '{} + {}i'.format(n2.p_real2, n2.p_imag2)

        p_real_resultante = self.p_real + n2.p_real2
        p_imag_resultante = self.p_imag + n2.p_imag2

        if p_imag_resultante < 0:
            print('A soma entre "{}" e "{}" é: {:.2f} - {:.2f}i'.format(num1, num2, p_real_resultante, -1 * p_imag_resultante))
        elif p_imag_resultante == 0:
            print('A soma entre "{}" e "{}" é: {:.2f}'.format(num1, num2, p_real_resultante))
        else:
            print('A soma entre "{}" e "{}" é: {:.2f} + {:.2f}i'.format(num1, num2, p_real_resultante, p_imag_resultante))

        print('-' * 60)

    # inicializa outro número, subtrai com o já inicializado e mostra o resultado na tela
    def subtrai(self):
        print('-' * 60)
        c = float(input('Digite a parte real do outro número complexo: '))
        d = float(input('Digite a parte imaginária do outro número complexo: '))
        n2 = NumerosComplexos()
        n2.inicializaNumero(c, d)
        n2.p_real2 = c
        n2.p_imag2 = d

        if self.p_imag < 0:
            num1 = '{} - {}i'.format(self.p_real, -1 * self.p_imag)
        elif self.p_imag == 0:
            num1 = self.p_real
        else:
            num1 = '{} + {}i'.format(self.p_real, self.p_imag)

        if n2.p_imag2 < 0:
            num2 = '{} - {}i'.format(n2.p_real2, -1 * n2.p_imag2)
        elif n2.p_imag2 == 0:
            num2 = n2.p_real2
        else:
            num2 = '{} + {}i'.format(n2.p_real2, n2.p_imag2)

        p_real_resultante = self.p_real - n2.p_real2
        p_imag_resultante = self.p_imag - n2.p_imag2

        if p_imag_resultante < 0:
            print('A subtração entre "{}" e "{}" é: {:.2f} - {:.2f}i'.format(num1, num2, p_real_resultante, -1 * p_imag_resultante))
        elif p_imag_resultante == 0:
            print('A subtração entre "{}" e "{}" é: {:.2f}'.format(num1, num2, p_real_resultante))
        else:
            print('A subtração entre "{}" e "{}" é: {:.2f} + {:.2f}i'.format(num1, num2, p_real_resultante, p_imag_resultante))

        print('-' * 60)

    # inicializa outro número, multiplica com o já inicializado e mostra o resultado na tela
    def multiplica(self):
        print('-' * 60)
        c = float(input('Digite a parte real do outro número complexo: '))
        d = float(input('Digite a parte imaginária do outro número complexo: '))
        n2 = NumerosComplexos()
        n2.inicializaNumero(c, d)
        n2.p_real2 = c
        n2.p_imag2 = d

        if self.p_imag < 0:
            num1 = '{} - {}i'.format(self.p_real, -1 * self.p_imag)
        elif self.p_imag == 0:
            num1 = self.p_real
        else:
            num1 = '{} + {}i'.format(self.p_real, self.p_imag)

        if n2.p_imag2 < 0:
            num2 = '{} - {}i'.format(n2.p_real2, -1 * n2.p_imag2)
        elif n2.p_imag2 == 0:
            num2 = n2.p_real2
        else:
            num2 = '{} + {}i'.format(n2.p_real2, n2.p_imag2)

        p_real_resultante = self.p_real * n2.p_real2 - self.p_imag * n2.p_imag2
        p_imag_resultante = self.p_real * n2.p_imag2 + self.p_imag * n2.p_real2

        if p_imag_resultante < 0:
            print('A multiplicação entre "{}" e "{}" é: {:.2f} - {:.2f}i'.format(num1, num2, p_real_resultante, -1 * p_imag_resultante))
        elif p_imag_resultante == 0:
            print('A multiplicação entre "{}" e "{}" é: {:.2f}'.format(num1, num2, p_real_resultante))
        else:
            print('A multiplicação entre "{}" e "{}" é: {:.2f} + {:.2f}i'.format(num1, num2, p_real_resultante, p_imag_resultante))

        print('-' * 60)

    # inicializa outro número, divide com o já inicializado e mostra o resultado na tela
    def divide(self):
        print('-' * 60)
        c = float(input('Digite a parte real do outro número complexo: '))
        d = float(input('Digite a parte imaginária do outro número complexo: '))
        n2 = NumerosComplexos()
        n2.inicializaNumero(c, d)
        n2.p_real2 = c
        n2.p_imag2 = d

        if self.p_imag < 0:
            num1 = '{} - {}i'.format(self.p_real, -1 * self.p_imag)
        elif self.p_imag == 0:
            num1 = self.p_real
        else:
            num1 = '{} + {}i'.format(self.p_real, self.p_imag)

        if n2.p_imag2 < 0:
            num2 = '{} - {}i'.format(n2.p_real2, -1 * n2.p_imag2)
        elif n2.p_imag2 == 0:
            num2 = n2.p_real2
        else:
            num2 = '{} + {}i'.format(n2.p_real2, n2.p_imag2)

        p_real_resultante = (self.p_real * n2.p_real2 + self.p_imag * n2.p_imag2) / (n2.p_real2 ** 2 + n2.p_imag2 ** 2)
        p_imag_resultante = (self.p_imag * n2.p_real2 - self.p_real * n2.p_imag2) / (n2.p_real2 ** 2 + n2.p_imag2 ** 2)

        if p_imag_resultante < 0:
            print('A divisão entre "{}" e "{}" é: {:.2f} - {:.2f}i'.format(num1, num2, p_real_resultante, -1 * p_imag_resultante))
        elif p_imag_resultante == 0:
            print('A divisão entre "{}" e "{}" é: {:.2f}'.format(num1, num2, p_real_resultante))
        else:
            print('A divisão entre "{}" e "{}" é: {:.2f} + {:.2f}i'.format(num1, num2, p_real_resultante, p_imag_resultante))

        print('-' * 60)
