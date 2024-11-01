import sys
import os

# Adiciona o diretório base do projeto ao PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.connection import get_connection

def callback(ch, method, properties, body):
    print(f"Dungeon Consumer recebeu: {body}")

connection = get_connection()
channel = connection.channel()
channel.queue_declare(queue='dungeon_queue')
channel.basic_consume(queue='dungeon_queue', on_message_callback=callback, auto_ack=True)
print("Dungeon Consumer aguardando mensagens.")
channel.start_consuming()
