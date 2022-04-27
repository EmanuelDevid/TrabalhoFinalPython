import glob
from datetime import datetime

class Nota(object):

    def __init__(self, id, tag, string):
        self.data = self.criaData()
        self.texto = str(string)
        self.tag = str(tag)
        self.id = str(id)

    #método criar data
    def criaData(self):
        date = datetime.now()
        data = str(date)
        return data


    #criando um arquivo txt da nota
    def criarNota(self):
        fileNome = str(self.id)
        file = open(fileNome, 'w')
        file.write('Tag(s): ' + self.tag + '\n')
        file.write('Data: ' + self.data + '\n')
        file.write('Texto: ' + self.texto + '\n')
        file.close()


    #adicionando as tags em um arquivo de texo
    def adicionandoTags(self, Tags):
        fileNome = str(self.id)
        file = open(fileNome, 'r')
        tags = file.readline()
        tags = tags.rstrip() + ', ' + Tags + '\n'
        data = file.readline()

        texto1 = str()
        for linha in fileNome:
            texto = file.readline()
            texto1 = texto1 + texto

        file = open(fileNome, 'w')
        file.write(tags)
        file.write(data)
        file.write(texto1)
        file.close()
        #atualizando os atributos da nota
        self.tag = tags
        self.texto = texto1


    # adicionando Novas as tags em um arquivo de texo
    def novaTag(self, Tags):
        fileNome = str(self.id)
        file = open(fileNome, 'r')
        tags = 'Tag(s): ' + Tags + '\n'
        file.seek(2)
        data = file.readline()

        texto1 = str()
        for linha in fileNome:
            texto = file.readline()
            texto1 = texto1 + texto

        file = open(fileNome, 'w')
        file.write(tags)
        file.write(data)
        file.write(texto1)
        file.close()
        #atualizando os atributos da nota
        self.tag = tags
        self.texto = texto1



    #adicionando texto em um arquivo de texo
    def adicionandoTexto(self, Texto):
        fileNome = str(self.id)
        file = open(fileNome, 'r')
        tags = file.readline()
        data = file.readline()
        texto1 = str()

        for linha in fileNome:
            texto = file.readline()
            texto1 = texto1 + texto

        texto1 = texto1.rstrip() + '\n' + Texto
        file = open(fileNome, 'w')
        file.write(tags)
        file.write(data)
        file.write(texto1)
        file.close()
        # atualizando os atributos da nota
        self.tag = tags
        self.texto = texto1


    #adicionando Novo texto em um arquivo de texo
    def novoTexto(self, Texto):
        fileNome = str(self.id)
        file = open(fileNome, 'r')
        tags = file.readline()
        data = file.readline()
        texto = 'Texto: ' + Texto + '\n'
        file = open(fileNome, 'w')
        file.write(tags)
        file.write(data)
        file.write(texto)
        file.close()
        # atualizando os atributos da nota
        self.tag = tags
        self.texto = texto

    # Consultando
    def consultar(self, opcao):
        fileNome = str(self.id)
        file = open(fileNome, 'r')
        tags = file.readline()
        data = file.readline()

        texto1 = str()
        for linha in fileNome:
            texto = file.readline()
            texto1 = texto1 + texto

        if opcao == 'tags':
            return tags
        if opcao == 'data':
            return data
        if opcao == 'texto':
            return texto1

    #verificar
    def verificar(self):
        ids = glob.glob("*.txt")
        i = 0
        var = False
        while i < len(ids):

            if(self.id == ids[i]):
                var = True
                if var == True:
                    break
            else:
                var = False
            i += 1
        return var

file = Nota('1234.txt', 'Bolo', 'bolo de cenoura eh muito bom')
file.criarNota()
file.adicionandoTags('qualquer coisa')
file.adicionandoTags('qualquer coisa22')
#file.novoTexto('Palmeiras n tem mundial')
#file.novoTexto('1111')

file.adicionandoTexto('palmeiras n tem mundial hahahaha')
file.adicionandoTexto('palmeiras n tem mundial kkkkk')
#file.novoTexto('1111')
#file.novaTag('zero')
#file.novaTag('zero1')
#print(file.consultar('texto'))
#file.adicionandoTexto('dmklfdjkkj')
#file.adicionandoTexto('dmklfdjkkj')
#print(file.consultar('texto'))'''
