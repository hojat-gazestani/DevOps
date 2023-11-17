import pika

params = pika.ConnectionParameters(
    host='rabbitmq',
    port=5672,
    virtual_host='/',
    credentials=pika.PlainCredentials('guest', 'guest'),
)

#params = pika.ConnectionParameters('amqp://guest:guest@rabbitmq:5672')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')

#def publish(method, body):
def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello') 

#publish()
connection.close()
