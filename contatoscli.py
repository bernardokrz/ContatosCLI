# Cria o dicionário de contatos
contact = {}
# Função que mostra lista de contatos cadastrados e seu número de telefone
def mostrar_contato():
    print("Nome\t\t\tTelefone")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

# Mensagem de inicialização
print("<ContatosCLI> Versão 1.0\npor Bernardo Krzysczak - krz02@proton.me\nSOFTWARE LIVRE PARA USO PESSOAL E COMERCIAL\n")

# Menu principal
while True:
    escolha = int(input("1. Novo contato\n2. Pesquisar contato\n3. Exibir contatos cadastrados\n4. Editar contato\n5. Apagar contato\n6. Sair\n\nEscolha a opção desejada: "))

# Opções do menu
    if escolha == 1:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone com DDD: ")
        contact[nome] = telefone
        print("\n**Contato cadastrado.\n")
    elif escolha == 2:
        procurar_nome = input("Digite o nome do contato: ")
        if procurar_nome in contact:
            print("\n**O número de",procurar_nome,"é:", contact[procurar_nome], "\n")
        else:
            print("\n**Contato não encontrado.")
    elif escolha == 3:
        if not contact:
            print("\n**Lista de contatos vazia!")
        else:
            print("-------------TODOS OS CONTATOS-------------")
            mostrar_contato()
    elif escolha == 4:
        editar_contato = input("Digite o nome do contato a ser editado: ")
        if editar_contato in contact:
            telefone = input("Digite o novo telefone com DDD: ")
            contact[editar_contato]=telefone
            print("\n**Contato atualizado.\n")
            mostrar_contato()
        else:
            print("\n**Contato não encontrado.")
    elif escolha == 5:
        apagar_contato = input("Digite o nome do contato a ser apagado: ")
        if apagar_contato in contact:
            confirmar = input("Tem certeza que deseja apagar este contato?(s/n): ")
            if confirmar == 's' or confirmar =='S':
                contact.pop(apagar_contato)
                print("\n**Contato apagado.\n")
            mostrar_contato()
        else:
            print("\n**Contato não encontrado.")
# Encerrando o programa
    else:
        print("**Encerrando...")
        break