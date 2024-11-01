# Multiplayer Game Notifications

Este projeto feito por mim - Rômulo Narcizo, implementa um sistema de notificações em tempo real para um jogo multiplayer RPG. Utiliza uma Topic Exchange para enviar notificações específicas para diferentes classes e locais.

## Estrutura de Pastas
- `producers/`: Scripts para envio de eventos (produtores).
- `consumers/`: Scripts para recebimento de notificações específicas (consumidores).
- `setup/`: Script de configuração das filas e bindings.
- `utils/`: Configuração de conexão com o servidor RabbitMQ.

## Executando o Projeto

1. Instale as dependências:
   ```bash
   pip install pika

2. Configure a conexão:

- Abra o arquivo utils/connection.py e altere a variável url para a URL do seu servidor RabbitMQ, como o CloudAMQP.

3. Configure as filas e bindings:

- No arquivo setup/setup_queues.py, estão definidos os bindings e as routing keys para cada classe e localização. Certifique-se de executar este script para configurar as filas antes de iniciar os produtores e consumidores.

4. Execute os produtores para enviar eventos de jogo:

- Produtores: Para enviar eventos de jogo, como batalhas ou a aparição de chefes, execute um dos scripts em producers/. Cada script representa um tipo de evento que será enviado para a Topic Exchange.

5. Execute os consumidores para receber notificações:

- Consumidores: Execute os scripts na pasta consumers/ para simular consumidores que representam jogadores específicos. Cada consumidor receberá apenas notificações relevantes conforme suas chaves de roteamento configuradas.

## Routing Keys

As routing keys configuram a entrega de mensagens específicas para cada consumidor:

- warrior.battle.near: Notificação de batalha próxima para guerreiros.
- mage.boss.spawned: Notificação de novo chefe para magos.
- dungeon.quest.warrior: Missão especial para guerreiros na masmorra.
- archer.forest.quest: Missão especial para arqueiros na floresta.

Essas chaves permitem que as mensagens sejam filtradas e direcionadas aos consumidores certos, garantindo que cada jogador receba apenas as notificações relevantes.
---