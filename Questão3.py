from datetime import datetime

nome_do_arquivo = "BlocoDeNotas.txt"

class BlocoDeNotas(object):

    def criar_nota(self, text, tags):
        now = datetime.now()
        file = open(nome_do_arquivo, 'a')
        id = str(sum(1 for line in open(nome_do_arquivo)) + 1)
        texto = id + ";" + text + ";" + tags + ";" + now.strftime("%d/%m/%Y") + "\n"
        file.writelines(texto)
        file.close()

    def modificar_nota(self, nota_id, modificar_tag_ou_nota, novo):
        with open(nome_do_arquivo, 'r') as file:
            texto = file.readlines()
        with open(nome_do_arquivo, 'w') as file:
            for i in texto:
                if texto.index(i) == nota_id - 1:
                    id, text, tags, data = i.split(";")
                    if modificar_tag_ou_nota == "1":
                        file.write(id + ";" + novo + ";" + tags + ";" + data)
                    elif modificar_tag_ou_nota == "2":
                        file.write(id + ";" + text + ";" + novo + ";" + data)
                    else:
                        file.write(id + ";" + text + ";" + tags + ";" + data)
                else:
                    file.write(i)

    def listar_notas(self):
        file = open(nome_do_arquivo, 'r')
        list = []
        for line in file:
            id, text, tags, data = line.split(";")
            list.append(Notas(id, text, tags, data))
        file.close()
        return list

    def listar_notas_filtro(self, tipo_filtro, filtro=""):
        file = open(nome_do_arquivo, 'r')
        list = []
        for line in file:
            id, text, tags, data = line.split(";")
            if tipo_filtro == "id":
                if id == filtro:
                    list.append(Notas(id, text, tags, data))
            elif tipo_filtro == "nota_tags":
                if filtro in text or filtro in tags:
                    list.append(Notas(id, text, tags, data))
            elif tipo_filtro == "create_date":
                if data == filtro + "\n":
                    list.append(Notas(id, text, tags, data))
        file.close()
        return list


class Notas(object):
    def __init__(self, id, text, tags, create_date):
        self.id = id
        self.text = text
        self.tags = tags
        self.create_date = create_date


def menu():

    b = BlocoDeNotas()

    while True:
        print("=" * 50)
        print("APLICAÇÃO SIMPLES DE UM BLOCO DE NOTAS:")
        print("1 - Criar nova nota")
        print("2 - Modificar nota")
        print("3 - Buscar notas")
        print("0 - sair")
        opcao = input("-> ")
        print("=" * 50)

        if opcao == "1":
            texto = input("Digite sua nota: ")
            tags = input("Digite tags para facilitar a busca da sua nota: ")
            b.criar_nota(texto, tags)

        elif opcao == "2":
            id = int(input("Digite o ID da nota que quer alterar: "))
            id_ou_tag = input("1 - Alterar o texto\n2 - Alterar as tags\n-> ")
            novo = input("Digite a alteração a ser feita: ")
            b.modificar_nota(id, id_ou_tag, novo)

        elif opcao == "3":
            print("1 - Buscar todas as notas")
            print("2 - Buscar nota por ID")
            print("3 - Buscar nota por texto ou tags")
            print("4 - Buscar pela data de criação da nota")
            sub_opcao = input("-> ")
            lista_retornada = []
            if sub_opcao == "1":
                lista_retornada = b.listar_notas()
            elif sub_opcao == "2":
                filtro = input("Digite o ID da nota desejada: ")
                lista_retornada = b.listar_notas_filtro("id", filtro)
            elif sub_opcao == "3":
                filtro = input("Digite o texto ou a tag da nota desejada: ")
                lista_retornada = b.listar_notas_filtro("nota_tags", filtro)
            elif sub_opcao == "4":
                filtro = input("Digite a data da criação da nota desejada: ")
                lista_retornada = b.listar_notas_filtro("create_date", filtro)
            else:
                print("Opção inválida, programa encerrado!")
                break

            print("=" * 60 + " NOTAS ENCONTRADAS " + '=' * 60 + '\n')
            for nota in lista_retornada:
                print("ID: " + nota.id + " - Nota: " + nota.text + " - Tags: " + nota.tags + " - Data de criação: " + nota.create_date)
            print("=" * 139)

        elif opcao == "0":
            print("Programa encerrado!")
            break
        else:
            print("Opção inválida!")

menu()
