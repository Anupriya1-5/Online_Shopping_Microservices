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
