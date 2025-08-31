# ALX Travel App with Celery

## Setup Instructions

### 1. Install RabbitMQ

```bash
# On Ubuntu/Debian
sudo apt-get update
sudo apt-get install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server

# On macOS
brew install rabbitmq
brew services start rabbitmq
