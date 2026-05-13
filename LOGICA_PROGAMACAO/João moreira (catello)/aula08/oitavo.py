# tratamento de erros e exceções
# valor1 = int(input("digite o primeiro valor:"))
# valor2 = int(input("digite o segundo valor:"))
# resultado = valor1 / valor2
# print(f"O resultado da divisão é {resultado}")

# Exemolo 1: tratamento de erros e exceções
# O código acima pode gerar um erro de divisão por zero se o usuário digitar 0 para o segundo valor. Para tratar esse erro, podemos usar um bloco try-except:
# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero.")

# Exemplo 2: tratamento de entrada invalida
# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except ValueError:
#     print("Erro de valor: Por favor, digite um número inteiro válido.")
# except ZeroDivisionError:
#     print("Erro: Não é possível dividir por zero.")

# Exemplo 3: Tratamento de múltiplas exceções
# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Ocorreu um erro: {e} ou Erro: Não é possível dividir por zero. {e}")

# Exemplo 4: Uso do bloco finally
# try:
#     valor1 = int(input("Digite o primeiro valor: "))
#     valor2 = int(input("Digite o segundo valor: "))
#     resultado = valor1 / valor2
#     print(f"O resultado da divisão é: {resultado}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Erro de value: Por favor, digite um número inteiro válido. {e} ou Erro: Não é possível dividir por zero. {e}")
# finally:
#     print("Bloco finally executado.")

#  Exercicio 1:
# Crie um algoritmo que pergunte o seu nome e trate erro ao inserir valores incorretos
# primeiro_nome = input("Digite seu primeiro nome: ")
# sobrenome = input("Digite seu sobrenome: ")
# try:
#     nome_completo = f"{primeiro_nome} {sobrenome}"
#     print(f"Olá, {nome_completo}!")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")

# # Exemplo 5: TypeError
# try:
#     resultado = "5" + 10
# except TypeError as e:
#     print(f"Erro de tipo: {e}")

# Exemplo 5: TypeError
# try:
#     resultado = "5" + 10
# except TypeError as e:
#     print(f"Erro de tipo: {e}")

# projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada 
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
# passo1:
# perguntar informações sobre o veiculo ou forma acesso
# pressionar o botao para emitir o carde verificar se 
# possui tag para acesso liberado se possuir erros
# informa ao usuario
# passo2:
# ferificaar o tempo de permanencia
# valor a se cobrado
# passo3:
# saida como sera?
# calcular tempo de permanencia se 
# for tag gerar ne fatura da tag
# pegar ticket
# devolver ticket na saida