markdown# Aula: Levantamento de Requisitos para Arquiteturas IoT

## 1. Desafios Específicos do Levantamento de Requisitos em IoT
*   **Aparato Físico e Digital:** Requisitos em IoT envolvem hardware (sensores/atuadores), firmware, redes de comunicação e software (nuvem/aplicativos).
*   **Restrições de Hardware:** Dispositivos IoT costumam ter baixo poder de processamento, pouca memória e limitação de energia (baterias).
*   **Volume de Dados:** Alta frequência de geração de dados que exige estratégias claras de armazenamento e descarte.

---

## 2. Requisitos nas Três Camadas da Arquitetura IoT

### Camada de Percepção (Hardware e Dispositivos)
*   **Requisito Funcional:** O sensor de temperatura deve realizar leituras a cada 5 segundos.
*   **Requisito Não-Funcional:** O dispositivo físico deve operar com baterias e consumir pouca energia, durando no mínimo 2 anos sem recarga.

### Camada de Rede e Transporte (Conectividade)
*   **Requisito Funcional:** O gateway deve transmitir dados para a nuvem via protocolo MQTT.
*   **Requisito Não-Funcional:** Em caso de perda de sinal de rede (Wi-Fi/Celular), o dispositivo deve armazenar até 24h de dados localmente (Edge Computing) e reenviar ao restabelecer a conexão.

### Camada de Aplicação (Nuvem e Usuário)
*   **Requisito Funcional:** O painel web deve exibir alertas visuais em tempo real quando a temperatura ultrapassar 40°C.
*   **Requisito Não-Funcional:** O sistema de nuvem deve ser capaz de receber e processar dados de 10.000 sensores simultaneamente (Escalabilidade).

---

## 3. Segurança e Protocolos como Requisitos Críticos

### Protocolos Leves de Comunicação
*   **MQTT e CoAP:** Protocolos assíncronos baseados em publish/subscribe, ideais para redes instáveis e dispositivos de baixo consumo.
*   **Mapeamento:** O analista deve especificar qual protocolo atende à restrição de banda da rede do cliente.

### Requisitos de Segurança em IoT
*   **Autenticação:** Cada dispositivo IoT deve possuir uma chave criptográfica única (certificados TLS) para se conectar à nuvem.
*   **Atualização (OTA - Over-The-Air):** O sistema deve permitir a atualização de firmware de todos os dispositivos remotamente e de forma segura.

---

## 4. Estudo de Caso Prático para a Aula

### Cenário: Sistema de Irrigação Inteligente
*   **Problema:** Uma fazenda precisa monitorar a umidade do solo para acionar bombas d'água automaticamente.
*   **Atividade dos Alunos:** Com base na arquitetura IoT de 3 camadas, divida o