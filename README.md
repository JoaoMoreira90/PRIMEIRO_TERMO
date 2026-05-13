# PRIMEIRO_TERMO
Material de aula 1°termo LOPAL- SOP- ARI- LER


## LOPAL
LOgica de programação python

### SOP

# Resumo Consolidado: Planejamento de Aulas de Levantamento de Requisitos

Este documento reúne todo o conteúdo pesquisado e estruturado para a disciplina de Engenharia de Software, focando no processo de Engenharia de Requisitos e suas interações com tecnologia, lógica e infraestrutura.

---

## Módulo 1: Fundamentos do Levantamento de Requisitos

### Técnicas de Elicitação de Requisitos
*   **Brainstorming:** Sessões focadas em geração de ideias em curto período. A regra fundamental é a ausência de críticas na fase inicial para maximizar a criatividade.
*   **Entrevistas:** Coleta de dados com stakeholders. Dividem-se em **Estruturadas** (perguntas fixas e métricas claras) e **Não-Estruturadas** (conversas livres para explorar fluxos complexos).

### Classificação de Requisitos
*   **Requisitos Funcionais (RF):** Descrevem o comportamento esperado do sistema (o que o sistema deve fazer). Exemplo: Emissão de relatórios em PDF.
*   **Requisitos Não-Funcionais (RNF):** Descrevem características de qualidade, restrições e atributos (como o sistema deve fazer). Exemplo: Tempo de carregamento inferior a 2 segundos.

### Modelagem e Documentação Técnica
*   **Diagramas de Casos de Uso (UML):** Representação visual dos atores, funcionalidades (casos de uso) e seus relacionamentos (`<<include>>`, `<<extend>>`).
*   **Prototipagem:** Validação de interface e UX. Divide-se em baixa fidelidade (wireframes em papel) e alta fidelidade (telas interativas no Figma).
*   **Relatórios Técnicos:** Uso da Especificação de Requisitos de Software (ERS), Matrizes de Rastreabilidade e definição de Critérios de Aceite.

---

## Módulo 2: Lógica de Programação Aplicada aos Requisitos

### Tradução de Regras de Negócio
*   **Estruturas Condicionais (Se-Então-Senão):** Mapeamento de critérios de decisão bi-direcionais no fluxo do negócio.
*   **Estruturas de Repetição (Loops):** Especificação de processamento de dados em lote ou varredura de coleções.

### Ferramentas de Validação Lógica
*   **Portugol (Pseudocódigo):** Linguagem intermediária em português para detalhar fluxos funcionais complexos antes da codificação.
*   **Tabelas de Decisão:** Matrizes que cruzam condições de entrada com ações do sistema para evitar a omissão de cenários alternativos e exceções.

---

## Módulo 3: Especificação de Requisitos voltada para Python

### Tipagem e Estruturas de Dados
*   **Mapeamento Nativo:** Associação de campos de cadastro a tipos Python como `String` (texto), `Int`/`Float` (valores numéricos e financeiros) e `Bool` (estados lógicos como `is_active`).
*   **Sintaxe de Negócio:** Aplicação direta de blocos `if/else` para validações e laços `for` para iteração de itens (ex: cálculo de carrinho de compras).

### Confiabilidade e Restrições Técnicas
*   **Tratamento de Exceções:** Uso de blocos `try/except` para capturar erros de entrada (como `ValueError`), garantindo o cumprimento de requisitos não-funcionais de integridade de dados.

---

## Módulo 4: Impacto dos Sistemas Operacionais (SO)

### O SO como Requisito Não-Funcional
*   **Restrição de Ambiente:** Definição de quais plataformas suportarão a aplicação (Windows, Linux, macOS, Android, iOS) e suas versões mínimas.

### Gerenciamento de Baixo Nível
*   **Processos e Concorrência:** Requisitos de desempenho traduzidos em *Multithreading* e multiprocessamento gerenciados pelo Kernel.
*   **Arquivos e Segurança:** Controle de acesso a dados locais através de permissões nativas do SO (diretivas `chmod` ou ACLs).
*   **Memória RAM:** Otimização para evitar o encerramento do software por falta de memória através de regras do *Out-Of-Memory (OOM) Killer*.

### Infraestrutura de Implantação
*   **Servidores vs. Clientes:** Diferenciação entre SO focado em interface/energia (Desktop/Mobile) e estabilidade/automação (Servidores).
*   **Virtualização:** Uso de contêineres **Docker** para isolar dependências e garantir portabilidade entre sistemas operacionais.

---

## Módulo 5: Arquitetura de Internet das Coisas (IoT)

### Particularidades de Projetos IoT
*   **Restrições Físicas:** Desafio de elicitar requisitos para hardware de baixo processamento, pouca memória e limitação de energia (baterias).

### Engenharia de Requisitos em 3 Camadas
1.  **Camada de Percepção:** Especificação de sensores, atuadores e frequência de leitura física.
2.  **Camada de Rede:** Uso de protocolos leves (MQTT, CoAP) e armazenamento local temporário em caso de queda de conexão (*Edge Computing*).
3.  **Camada de Aplicação:** Processamento em nuvem, dashboards e requisitos de alta escalabilidade (suporte a milhares de dispositivos simultâneos).

### Segurança e Manutenção
*   **Autenticação Robusta:** Uso de chaves criptográficas exclusivas e certificados TLS por dispositivo.
*   **Atualização remota (OTA):** Requisito essencial de infraestrutura para correção de firmwares à distância via *Over-The-Air*.