markdown# Aula: Levantamento de Requisitos e Sistemas Operacionais (SO)

## 1. O Sistema Operacional como Requisito Não-Funcional
*   **Restrição de Ambiente:** Determina em quais plataformas o software deve rodar (Ex: Windows, Linux, macOS, Android, iOS).
*   **Impacto no Desenvolvimento:** O SO escolhido dita quais linguagens, frameworks e ferramentas de compilação serão utilizados pela equipe técnica.
*   **Compatibilidade:** Define as versões mínimas de suporte (Ex: "O aplicativo deve ser compatível com Android 10 ou superior").

---

## 2. Traduzindo Requisitos do Sistema Operacional

### Gerenciamento de Processos e Concorrência
*   **Requisito de Desempenho:** "O sistema deve processar requisições em segundo plano sem travar a interface do usuário."
*   **Visão do SO:** Uso de *Multithreading* (múltiplas linhas de execução) e multiprocessamento gerenciados pelo núcleo (kernel) do sistema.

### Gerenciamento de Arquivos e Permissões
*   **Requisito de Segurança:** "O sistema deve salvar relatórios localmente e garantir que apenas o usuário administrador possa editá-los."
*   **Visão do SO:** Controle de permissões do sistema de arquivos (Ex: diretivas `chmod` no Linux ou ACLs no Windows).

### Gerenciamento de Memória
*   **Requisito de Restrição:** "O software deve rodar em dispositivos móveis limitados com menos de 2GB de memória RAM disponível."
*   **Visão do SO:** Otimização do uso de memória e tratamento para evitar o encerramento do app pelo *Out-Of-Memory (OOM) Killer* do SO.

---

## 3. Arquitetura e Infraestrutura de Sistemas

### Sistemas Operacionais de Servidor vs. Cliente
*   **Cliente (Desktop/Mobile):** Foco na experiência do usuário, gerenciamento de energia e interface gráfica (Ex: Windows 11, iOS).
*   **Servidor:** Foco em estabilidade, automação e alto volume de acessos simultâneos sem interface gráfica (Ex: Ubuntu Server, Red Hat).

### Portabilidade e Virtualização
*   **Containers (Docker):** Técnica para isolar a aplicação e suas dependências, garantindo que o software funcione igual em qualquer sistema operacional.

---

## 4. Estudo de Caso para Discussão em Aula

### Cenário: Aplicativo de Monitoramento de Frotas
*   **Requisito Funcional:** O app deve rastrear a localização do veículo via GPS em tempo real.
*   **Desafio do SO:** Os sistemas operacionais modernos (como iOS e Android) sus