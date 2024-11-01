import pika

def get_connection():
    url = 'amqps://amdneafp:FPrRFUb84tzVmKcdkNOUp_HYropW3v3g@jackal.rmq.cloudamqp.com/amdneafp'
    params = pika.URLParameters(url)
    return pika.BlockingConnection(params)