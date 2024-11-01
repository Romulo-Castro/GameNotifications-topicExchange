import sys
import os

# Adiciona o diretório base do projeto ao PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.connection import get_connection

def callback(ch, method, properties, body):
    print(f"Boss Consumer recebeu: {body}")

connection = get_connection()
channel = connection.channel()
channel.queue_declare(queue='boss_queue')
channel.basic_consume(queue='boss_queue', on_message_callback=callback, auto_ack=True)
print("Boss Consumer aguardando mensagens.")
channel.start_consuming()
