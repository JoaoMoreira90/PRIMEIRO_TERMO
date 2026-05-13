# REVISÃO DO CONTEUDO
# print = "função de saida de dados para o console"
# input = "Função de entrada de dados do usuário via teclado"
# if ="Estrutura de decisão para executar código condições"
#    elif = "combinação de else + if para verificar múltipas condições"
#    else = " parte opcional de um if que executa código quando a condição do if é falsa"
# for = "laço repetitivvo"



# Exemplo 1: com print e input
# nome = input("Digite seu nome: ")
# print(f"olá, {nome}! Bem-vindo à aula de python para desenvolvimento de Sistema")

# Exemplo 2:com if, elif e else
# nota = float(input("digite a nota do aluno: "))
# if nota >= 7:
#     print("aluno aprovado!")
# elif  nota >= 5:
#     print("Aluno em recuperação")
# else:
#     print("Aluno reprovado")




# Exemplo 3: com for
# materiais = ["metal", "plastico", "vidro"]
# for material in materiais:
#     print(f"processando material: {material}.")
#     print(f"material {material} processando com sucesso")
# print("Fim do processamento de materiais")



# 2. O laço while(Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de
# uma condição (como um sensor de segurança ou um botão de emergência).
# Exemplo: monitor de temperatura (loop infinito contrlado)
# Repete enquanto a temperatura estiver segura
# import time
# temperatura = 25
# while temperatura < 40:
#     print(f"temperatura atual: {temperatura}°C. Sistema operando...")
#     time.sleep(1)
#     temperatura += 3 #Simulando o aquecimento da máquina
# print("ALERTA! temperatura atingindo o limite. Desligando o  motor...")

# Lista de temperatura lidas pelo sensor por minutos
# leituras = [70, 75, 82, 98, 110, 85, 80]
# for temp in leituras:
#     while temp > 100:
#         print(f"CRÍTICO: {temp}°C detactado! Acionado parada de emergência.")
#         break # O loop para aqui e NÂO lê os próximos valores (85 e 80)
#     print(f"Temperatura está em {temp}°C. Operação normal.")
# print("Sistema desligado. Agauardando manutenção")


# # produção de peças com controle de material usando continue
# materiais = ["material", "metal","plastico", "metal", "vidro", "metal"]
# for peca in materiais:
#     if peca != "metal":
#         print(f"Aviso: peça de {peca} detectada. Desviando para descarte...")
#         continue # Pula o restante de código abaixo e vai para a próxima peça
#     #Esta código só roda se a peça for de metal
#     print(f"processando peça de {peca}. Furando e polindo...")
# print("Fim do lote de produção")

