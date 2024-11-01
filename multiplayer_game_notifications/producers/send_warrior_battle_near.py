import sys
import os

# Adiciona o diretório base do projeto ao PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.connection import get_connection

connection = get_connection()
channel = connection.channel()
channel.basic_publish(exchange='game.notifications', routing_key='warrior.battle.near', body='Batalha próxima aos guerreiros')
print("Evento enviado: 'Batalha próxima aos guerreiros'")
connection.close()