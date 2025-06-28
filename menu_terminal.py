from   InquirerPy import prompt
import os
import shutil
while True:
    perguntas=[
    {
        'type':'list',
        'name':'ação',
        'message':'oq vc deja fazer?',
        'choices':['criar arquivo',
                   'editar arquivo',
                   'ler arquivo',
                   'limpar arquivo',
                   'criar copia',
                    'sair']



    }
]
    resposta=prompt(perguntas)
    escolha=resposta['ação']
    if escolha == "sair":
        print("Encerrando programa...")
        break

    nome_arquivo = input("Digite o nome do arquivo (ex: meu_arquivo.txt): ")

    if escolha == "criar arquivo":
        if os.path.exists(nome_arquivo):
            print("Arquivo já existe.")
        else:
            with open(nome_arquivo, 'w') as f:
                print(f"Arquivo '{nome_arquivo}' criado com sucesso.")

    elif escolha == "editar arquivo":
        if not os.path.exists(nome_arquivo):
            print("Arquivo não encontrado.")
        else:
            conteudo = input("Digite o conteúdo que deseja adicionar: ")
            with open(nome_arquivo, 'a') as f:
                f.write(conteudo + '\n')
            print("Conteúdo adicionado com sucesso.")

    elif escolha == 'ler arquivo':
        if not os.path.exists(nome_arquivo):
            print("Arquivo não encontrado.")
        else:
            with open(nome_arquivo, 'r') as f:
                print("\n--- Conteúdo do Arquivo ---")
                print(f.read())

    elif escolha == "limpar arquivo":
        if not os.path.exists(nome_arquivo):
            print("Arquivo não encontrado.")
        else:
            with open(nome_arquivo, 'w') as f:
                pass
            print(f"Arquivo '{nome_arquivo}' limpo com sucesso.")

    elif escolha ==  'criar copia':
        if not os.path.exists(nome_arquivo):
            print("Arquivo não encontrado.")
        else:
            novo_nome = input('digite o nome da sua copia:(EX:copia.txt)')
            if not  novo_nome.endswith('.txt'):
                novo_nome=novo_nome+'.txt'

            shutil.copy(nome_arquivo, novo_nome)
            print(f"Cópia criada: {novo_nome}")

    else:
        print("Opção inválida!")