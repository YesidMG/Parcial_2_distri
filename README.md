# Microservices Application

This project implements a microservices architecture using Docker Compose. It consists of an API service, a worker service, RabbitMQ for message queuing, and Traefik as a reverse proxy.

## Project Structure

```
microservices-app
├── api
│   ├── app.py                # Implementation of the REST API
│   ├── requirements.txt      # Dependencies for the API
│   └── Dockerfile            # Dockerfile for the API service
├── worker
│   ├── worker.py             # Logic for consuming messages from RabbitMQ
│   ├── requirements.txt      # Dependencies for the worker
│   └── Dockerfile            # Dockerfile for the worker service
├── traefik
│   └── traefik.yml           # Configuration for Traefik reverse proxy
├── data
│   └── .gitkeep              # Keeps the data directory in version control
├── docker-compose.yml         # Orchestrates all services
└── README.md                 # Documentation for the project
```

## Services

### API Service
- **Endpoint**: `POST /message`
- **Functionality**: Receives a JSON body and publishes the message to a RabbitMQ queue named `messages`. The endpoint is secured with basic authentication.

### Worker Service
- **Functionality**: Listens to the `messages` queue in RabbitMQ and writes the content of the messages to a local file. It uses a volume for data persistence.

### RabbitMQ
- **Functionality**: Message broker that facilitates communication between the API and the worker.

### Traefik
- **Functionality**: Acts as a reverse proxy, routing requests to the appropriate services. It routes `/api` to the API service and `/monitor` to the RabbitMQ web interface.

## Getting Started

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd microservices-app
   ```

2. **Build and run the services**:
   ```
   docker-compose up --build
   ```

3. **Access the API**:
   - The API will be available at `http://localhost/api/message`.

4. **Monitor RabbitMQ**:
   - Access the RabbitMQ management interface at `http://localhost/monitor`.

## Requirements

- Docker
- Docker Compose

## License

This project is licensed under the MIT License.