import sys
import os

# Adiciona o diretório base do projeto ao PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.connection import get_connection

def setup_queues():
    # Estabelece a conexão com RabbitMQ
    connection = get_connection()
    channel = connection.channel()

    # Declaração da exchange do tipo 'topic'
    channel.exchange_declare(exchange='game.notifications', exchange_type='topic')

    # Declaração das filas
    queues = [
        'warrior_queue', 'mage_queue', 'archer_queue',
        'forest_queue', 'desert_queue', 'dungeon_queue',
        'battle_queue', 'boss_queue'
    ]

    # Criação e configuração de cada fila
    for queue in queues:
        channel.queue_declare(queue=queue)

    # Bindings de acordo com as routing keys
    bindings = {
        'warrior_queue': 'warrior.battle.near',
        'mage_queue': 'mage.boss.spawned',
        'archer_queue': 'archer.*',
        'forest_queue': 'forest.*',
        'desert_queue': 'desert.*',
        'dungeon_queue': 'dungeon.*',
        'battle_queue': '*.battle.*',
        'boss_queue': '*.boss.*'
    }

    # Configura os bindings
    for queue, routing_key in bindings.items():
        channel.queue_bind(exchange='game.notifications', queue=queue, routing_key=routing_key)

    print("Filas e bindings configurados com sucesso.")
    
    # Fecha a conexão
    connection.close()

if __name__ == "__main__":
    setup_queues()
