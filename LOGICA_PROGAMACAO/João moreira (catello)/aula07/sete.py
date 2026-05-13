# # Solicitando os dados do jogador
# # nick_jogador = input("digite o nome do jogador:")
# # nivel_jogador = input("digite o niver do jogador que ele esta:")

# # # Exibindo a mensagem formatada
# # print(f"\nO jogador {nick} esta no nivel que ele parou {nivel} e esta pronto para começar! :)")



# # Passo 1: Pergunta o valor da mesada semanal
# # valor_semanal = float(input("Quanto você ganha de mesada por semana? R$ "))

# # # Passo 2: Calcula o valor mensal (multiplicando por 4)
# # valor_mensal = valor_semanal * 4

# # # Passo 3: Exibe o resultado
# # print(f"No final do mês, você terá: R$ {valor_mensal:.2f}")


# # manipulação de arquivo e texto
# # TEXTO = " Python é Muito legal!"
# # prinit(texto.strip().upper());# " Python "
# # manipular_texto = " Python é Muito legal! "
# # print(manipular_texto.strip().upper());# " Python 
# # print(manipular_texto.strip().upper());# " Python 
# # print(manipular_texto.strip().upper());# " Python 
# # print(manipular_texto.strip().startswith("A"))# começar com letra inicial
# # print(manipular_texto.strip().capitalize())# " letras inicíal "
# # print(manipular_texto.strip().title())# " Titulo "
# # print(manipular_texto.strip().replace("","_")) # " preencher vazios "
# # print(manipular_texto.strip().split())# " Separar palavras "



# # Q1
# # crie um programa que peça ao usuário para inserir uma frase e,
# # em seguida, exiba a frase com as seguintes transformações:
# # - deixe o texto em letras minuscula
# # frase_usuario = input("digite uma frase: ")
# # print(frase_usuario.strip().lower())

# # manipular aquivo:
# # Escrevendo
# # with open ("notas.txt", "w", encoding="utf-8") as texto:
# #     texto.write("estudar python hoje!")
# #     texto.write("\nLer sobre clean code.")
# #     texto.write("\n Estamos evoluindo.")

# # Lendo
# # with open ("notas.txt", "r", encoding="utf-8") as texto:
# #     conteudo = texto.read()
# #     print(conteudo)

# # exemplo 1
# # Crie um progama  que leia o conteudo de um arquivo de texto
# # e conte quantas vezes a palavra "python" aparece no arquivo. Exiba
# # o resultadopara o usuário.
# print("Contagem de palavras em arquivo")
# with open ("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     contagem = conteudo.count("python")
#     contagem = conteudo.upper().count("PYTHON") # contar a palavra python
#     contagem = conteudo.lower().count("python")
#     print(f"a conyagem de palavras {contagem} é de...") 

# Interação com o sistema operacional
# import os # importa o módulo os para interagir com o sistema operacional

# Onde estou?
# print(os.getcwd())

# print(os.listdir())
# print(os.listdir("C:/Users"))

# criar pastas
#os .mkdir("nova_pasta")

# Renomear pasta
#os.rename("João", "Minha_pasta")

# apagar pastas
#os.rmdir("Minha_pasta")
# os.remove("notas.txt") #Excluir arquivos


