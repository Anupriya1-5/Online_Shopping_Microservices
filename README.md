# Online Shopping Microservices

## Aim

To develop an Online Shopping application using microservices and analyze its performance using Docker and workload testing.

## Microservices

The project contains three microservices:

- **Product Service** – Port 5000
- **User Service** – Port 5001
- **Order Service** – Port 5002

## Architecture

```text
                 Client
                    |
                    v
             Order Service
                Port 5002
                /       \
               /         \
              v           v
     Product Service   User Service
        Port 5000        Port 5001
```
## Technologies Used
- Python
- Flask
- REST API
- Docker
- Docker Compose
- Requests
## Project Structure
OnlineShoppingMicroservices/
│
├── product-service/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── user-services/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── order-services/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── docker-compose.yml
├── load_test.py
└── README.md
## Product Service
Manages product information.
GET /products
GET /products/<id>
GET /health
Port:
5000
## User Service
Manages user information.
GET /users
GET /users/<id>
GET /health
Port:
5001
## Order Service
Creates orders and communicates with the Product and User Services.
POST /orders
GET /orders
GET /health
Port:
5002
## Dockerization
Build the Docker images:
docker compose build
Start the services:
docker compose up -d
Check running containers:
docker ps
## Inter-Service Communication
The Order Service communicates with both Product Service and User Service.
Order Service
     |
     +----> Product Service
     |
     +----> User Service
Test an order:
curl -X POST http://127.0.0.1:5002/orders -H "Content-Type: application/json" -d "{\"user_id\":1,\"product_id\":1,\"quantity\":2}"
## Workload Testing
Five workload levels were tested:
| Workload | Concurrent Requests |
|---|---:|
| W1 | 1 |
| W2 | 2 |
| W3 | 4 |
| W4 | 8 |
| W5 | 16 |


## Performance Analysis
- Throughput increased as concurrency increased.
- Response time increased at higher workload levels.
- No requests failed during testing.
- Order Service was the relatively resource-heavy service.
- At higher concurrency, throughput improvement became smaller.
## Conclusion
The Online Shopping microservices application was successfully developed, Dockerized, deployed, and tested.
The three services communicated successfully with each other.
A total of 2500 requests were tested, and all requests were completed successfully.
The experiment showed that increasing concurrency improves throughput, while response time increases at higher workload levels.
```
