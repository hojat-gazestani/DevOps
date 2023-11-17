import pika

params = pika.ConnectionParameters(
    host='rabbitmq',
    port=5672,
    virtual_host='/',
    credentials=pika.PlainCredentials('guest', 'guest'),
)

# params = pika.ConnectionParameters('amqp://guest:guest@rabbitmq:5672')
connection = pika.BlockingConnection(params)
channel = connection.channel()

try:
    channel.queue_declare(queue='admin')

    def callback(ch, method, properties, body):
        print('Received in admin')
        print(body)

    channel.basic_consume(queue='admin', on_message_callback=callback)

    print("Started Consuming")

    channel.start_consuming()

except Exception as e:
    print(f"Error: {e}")

finally:
    # Ensure to close the connection when done
    connection.close()

