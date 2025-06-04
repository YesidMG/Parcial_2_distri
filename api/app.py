from flask import Flask, request, jsonify
import pika
import os
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.getenv('BASIC_AUTH_USERNAME', 'user')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('BASIC_AUTH_PASSWORD', 'password')
basic_auth = BasicAuth(app)

def publish_message(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='messages')
    channel.basic_publish(exchange='', routing_key='messages', body=message)
    connection.close()

@app.route('/api/message', methods=['POST'])
@basic_auth.required
def message():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    publish_message(data['message'])
    return jsonify({'status': 'Message sent'}), 200

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)