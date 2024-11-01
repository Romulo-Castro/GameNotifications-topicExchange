import sys
import os

# Adiciona o diretório base do projeto ao PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.connection import get_connection

connection = get_connection()
channel = connection.channel()
channel.basic_publish(exchange='game.notifications', routing_key='dungeon.quest.warrior', body='Missão especial para guerreiros na masmorra')
print("Evento enviado: 'Missão especial para guerreiros na masmorra'")
connection.close()