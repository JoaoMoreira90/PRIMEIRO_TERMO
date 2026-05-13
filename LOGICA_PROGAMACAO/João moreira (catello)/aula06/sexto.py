# 1 
# print("Registro de veículo")
# modelo = input("Qual é o modelo do veículo....")
# placa  = input("Qual é a placa do veículo....")
# print(f"veículo {modelo} de placa {placa} registre no sistema. boa viagem!")

# # 2
# print("Cálculo de Autonomia")
# tanque = float(input("Qual é a capacidade de seu tanque em litros"))
# consumo = float(input("Digite o comsumo médio por caminhão km/L"))
# total = tanque / consumo
# print(f"Seu caminhão pode percorrer {total:.2f} em km/L")
# print("Seu caminhão pode percorrer", round(total,2), "em km/L")

# 3
# print("Conversor de Moeda (Frente Internacional)")
# valor_reais = float(input("Qual é o valor em Reais que sára convertito?"))
# taxa_dolar = float(input("Qual é o valor da taxa em dolar em Reais?..."))
# total = valor_reais / taxa_dolar
# print(f"O valor total convertido é... {total:.2f}")

# 4
# print("Média de entrega")
# tempo1 = int(input("Qual foi o tempo para concluir a rota 1 em horas"))
# tempo2 = int(input("Qual foi o tempo para concluir a rota 2 em horas"))
# tempo3 = int(input("Qual foi o tempo para concluir a rota 3 em horas"))
# media = (tempo1 + tempo2 + tempo3) / 3
# print(f"A médidia {media:.2f} de tempo das entregas")

# 5
# print("Monitor de carga")
# peso = float(input("Qual é o peso  atual do seu caminhão?..."))
# if peso < 10:
#     print("Carga leve")
# if peso <= 25:
#     print("carga padrão")
# else:
#     print("ALERTA: Exceso de peso!!...")

# 6
# print("Classificador de Destino")
# print("Regiões = N - Região norte , s - Região sul , Qualquer outra - internacional")
# regiao = input("Inserir o codigo da região: "). lower()
# if regiao == "N" . upper() or regiao == "n" .lower():
#     print("Região Norte")
# elif regiao == "S":
#     print("Região Sul")
# else:
#     print("Região Internacional")

# 7
# print("Liberação de Saída")
# checklist = input("O checklist foi concluído? [concluído ou não concluido]")
# motorista = input("O motorista foi identificado? [Sim ou Não]")
# if checklist == "Concluído" and motorista == "Sim":
#     print("Veículo autorizado a iniciar a rota.")
# else:
#     print("Veículo NÃO autorizado a incluir a rota. Verificar checklist e identicação do motorista.")

# 8
# print("Cálculo de Atrasos")
# toatl_entregas = int(input("total de Entrgas Agendadas:..."))
# toatl_atrasos = int(input("total de Entrgas Atrasos:..."))
# if toatl_atrasos > toatl_entregas * 0.1:
#     print("Necessário otimizar rotas")
# else:
#     print("Logística Eficiente")

# 9
# print("Validação de Calibragem")
# pressao = float(input("Digite a pressão dp pneu em PSI:..."))
# if 100 <= 110:
#     print("Dentro do padrão")
# elif pressao < 100:
#     print("Abaixo de recomendado")
# else:
#     print("Acima do recomendado")

# 10
# print("Contagem de Embarque")
# import time
# for contagem in range(5,0,-1):
#     time.sleep(1)
#     print(contagem)
# print("Portão trancado")

# 11
# print("Somatorio de frete (Acumulatorio) versão 1")
# total = 0
# while True:
#     valor = float(input("Valor do Frete:"))
#     if valor == 0:
#         total += valor
#         print(f"total acumulado {total} de frete")

# print("versão - 2")
#  faturamento_total = 0
# valor_frente = -1

# while valor_frete !=0:
#     valor_frete = float(input("Valor do frete ou 0 para encerrar"))
#     faturamento_total += valor_frete
#     print(f"Faturamento acumulado: R$ {faturamento_total}")
# print("Cáculo executado com sucesso")

# print("Somatório de Frente (Acumulativo) - Versão 3")
# b = 0
# while True:
#     t = int(input("Valor Frete...")
#             c = input("Quar continuar s/n")
#             b += try
#             if c == "s":
#             continue
#             else
#             break
#             print(f"Faturamento total{b}acumulado")

# 12
# print("Monitoramento de frota")
# maior_km = 0
# for frota in range(1, 6):
#     km = float (input(f"Digite a quilometragem do veículo {frota}:"))
#     if km > maior_km
#     maior_km = km
#     print(f"A maior quilometragem regidtrada é: {maior_km} km.")

# 13
# print("Sistema de Rastreio")
# codigo_correto = "track99"
# tentativas = 0
# max_tentativa = 3
# while tentativas < max_tentativas:
#     codigo_input = input("Código de acesso para o rastreador: :)")
#     if codigo_input == codigo_correto:
#         print("Acesso permitido. Iniciado rastreamento...")
#         break
# else:
#     tentativas += 1
#     print("Acesso negado")
#     if tentativas < max_tentativa:
#         print(f"Tentativa restantes: {max_tentativa-tentativas}")

#     else:
#         print("Rastreamento bloqueado")
