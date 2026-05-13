markdown# Aula: Levantamento de Requisitos e Lógica de Programação com Python

## 1. Mapeamento de Requisitos para Tipos de Dados Python
*   **Texto (String):** Requisitos que envolvem campos de cadastro (Ex: Nome, CPF, E-mail).
*   **Numéricos (Int/Float):** Regras de negócio com valores monetários, idade ou contadores.
*   **Booleanos (Bool):** Requisitos de ativação ou estados binários (Ex: `is_active`, `tem_permissao`).

---

## 2. Traduzindo Requisitos Funcionais em Sintaxe Python

### Condicionais (Mapeamento de Regras de Negócio)
*   **Requisito:** "Se o valor da compra for maior que R\$ 200, aplique frete grátis. Caso contrário, cobre R\$ 20."
*   **Código Python:**
    ```python
    if valor_compra > 200.00:
        frete = 0.00
        print("Frete Grátis aplicado.")
    else:
        frete = 20.00
    ```

### Loops (Processamento de Requisitos em Lote)
*   **Requisito:** "O sistema deve varrer a lista de produtos do carrinho e calcular a soma total."
*   **Código Python:**
    ```python
    carrinho = [29.90, 49.90, 15.00]
    total = 0.0

    for preco in carrinho:
        total += preco
    
    print(f"Total da compra: R$ {total:.2f}")
    ```

---

## 3. Validando Restrições (Requisitos Não-Funcionais)

### Segurança e Tipagem com Python
*   **Requisito:** "O sistema deve garantir que a idade fornecida seja um número inteiro para evitar falhas no banco de dados."
*   **Código Python (Tratamento de Exceções):**
    ```python
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Erro: O requisito do sistema exige um número inteiro válido.")
    ```

---

## 4. Exercício Prático de Aula

### Cenário: Sistema de Cadastro e Acesso Integrado
*   **Enunciado:** Escreva um script Python que valide se um usuário inseriu o e-m