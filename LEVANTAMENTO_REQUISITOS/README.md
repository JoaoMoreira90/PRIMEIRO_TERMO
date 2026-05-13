markdown# Aula: Levantamento de Requisitos de Software

## 1. Técnicas de Elicitação de Requisitos

### Brainstorming
*   **Objetivo:** Gerar o maior número de ideias e insights em um curto período.
*   **Regra de Ouro:** Foco em quantidade, proibindo críticas na fase inicial de ideação.
*   **Participantes:** Engenheiros de software, gerentes de produto, stakeholders e usuários finais.

### Entrevistas
*   **Objetivo:** Coletar visões detalhadas, expectativas e dores de um stakeholder específico.
*   **Estruturada:** Questionário fixo focado em dados objetivos e métricas claras.
*   **Não-Estruturada:** Conversa livre ideal para explorar problemas complexos e fluxos informais.

---

## 2. Classificação de Requisitos

### Requisitos Funcionais (RF)
*   **Definição:** Descrevem o que o sistema deve fazer (comportamento e funções).
*   **Exemplo 1:** O sistema deve permitir o cadastro de usuários via e-mail.
*   **Exemplo 2:** O sistema deve emitir relatórios de vendas em formato PDF.

### Requisitos Não-Funcionais (RNF)
*   **Definição:** Descrevem como o sistema deve fazer (qualidade, restrições e atributos).
*   **Exemplo 1:** A página de checkout deve carregar em menos de 2 segundos.
*   **Exemplo 2:** Todas as senhas devem ser criptografadas com o algoritmo SHA-256.

---

## 3. Modelagem e Visualização

### Diagramas de Casos de Uso (UML)
*   **Atores:** Entidades externas que interagem com o sistema (usuários ou outros sistemas).
*   **Casos de Uso:** Funcionalidades ou serviços fornecidos pelo sistema ao ator.
*   **Relacionamentos:** Conexões de inclusão (`<<include>>`), extensão (`<<extend>>`) e associação.

### Prototipagem
*   **Baixa Fidelidade:** Desenhos em papel (wireframes) para validar fluxos rapidamente.
*   **Alta Fidelidade:** Protótipos interativos (Figma/Adobe XD) idênticos ao produto final.
*   **Propósito:** Validar a interface e a experiência do usuário (UX) antes do código.

---

## 4. Documentação

### Relatórios Técnicos
*   **Especificação de Requisitos de Software (ERS):** Documento formal que consolida o escopo.
*   **Matriz de Rastreabilidade:** Tabela que conecta cada requisito à sua origem e código.
*   **Critérios de Aceite:** Regras claras que determinam se o requisito foi ate