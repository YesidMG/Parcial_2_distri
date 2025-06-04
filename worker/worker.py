import pika
import os
import time

def callback(ch, method, properties, body):
    message = body.decode('utf-8')
    os.makedirs('data', exist_ok=True)
    with open(os.path.join('data', 'messages.log'), 'a') as f:
        f.write(f"{message}\n")
    print(f"Received message: {message}", flush=True)

def wait_for_rabbitmq(max_retries=10, delay=5):
    for i in range(max_retries):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
            return connection
        except pika.exceptions.AMQPConnectionError:
            print(f"RabbitMQ no disponible, reintentando en {delay} segundos... ({i+1}/{max_retries})")
            time.sleep(delay)
    raise Exception("No se pudo conectar a RabbitMQ después de varios intentos.")

def main():
    connection = wait_for_rabbitmq()
    channel = connection.channel()
    channel.queue_declare(queue='messages')
    channel.basic_consume(queue='messages', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C', flush=True)
    channel.start_consuming()

if __name__ == "__main__":
    main()