# 1. o laço 'for' (respetição determinadas)
# Use o 'for' quando você sabe exatemente quantas vezes deve acontecer (como ler 10 sensores ou processar uma lisa de peças).
# Exemplo:Relatoerio de produção Diaria
# imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# exemplo 1
# for lote in range(1,6):
#     print(f"processando lote número{lote}...")
#     print("qualidade verificade [OK]")
#     print("produção do dia finalizada!")

# exemplo 2
# for b in range(10)
# print(f"Quantidade total {b} foi...")



# exemplo 3 
# imagine o seguinto cenário, iremos produzir 20 discos de vinil
# for vinir in range(1,21):
#     print(f"produção de {vinir}, diaria")

    # exeplo 4
# pecas = ["engranagem", "Eixo", "Rolamento", "parafuso", "martelo", "prego", "chave de fenda", "alicate"]
# itempecas = ["cilindrica", "duplo", "cônica", "prego", "Orelha", "redondo", "phillips", "Universal"]


# for item in pecas:
#     print(f"item em estoque: {item}")




# exemplo 5
# clovis = input("qual carro você quer")
# nissan = ["nissan gtr r 34","Nissan Kicks","Nissan Versa","Nissan Frontier"]
# for item in nissan:
#     print(f"qual e a o nome do carro {item} ")

# exercico 1
# uma estrategia processa 10 peças por ciclo. crie um programa que use um for para contar de 1 e 10 e, para cade número, 
# imprima "peça n° x processada com sucesso" . no final, exiba ciclo de produção concluido

# for ciclo in range(1,11):
#     print(f"peça n° {ciclo} pprocessada co sucesso... :)")
# print("ciclo de produção concluido... :)")


# exercico 2 
# print("Está e sua lista de compras:")
# for banana in range(1,11):
#     print(f"banana n°{banana}")
# print("------------")
# for manga in range(1,6):
#     print(f"manga n°{manga}")
# print("------------")
# for melancia in range(1,6):
#     print(f"melancia n°{melancia}")
# print("------------")
# for abacaxi in range(1,6):
#     print(f"abacaxi n°{abacaxi}")
# print("------------")
# total = banana + manga + melancia + abacaxi
# print("Foram produzidos: \n", round(total,2))

# exercico 3
# print("tabuada")
# tab = int(input("digite qual tabuada você quer:"))
# for numero in range(1,11):
#     resultado = tab * numero
#     print(f"{tab} x {numero} = {resultado}")