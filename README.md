# Microservices

A microservice that make a request to another microservice and store their data into storage for caching

## Documentation

The documentation for python-service its located under /docs on 127.0.0.1:8000

## Usage

Just execute:
```bash
docker-compose up -d
```

## Tests

Just enter on a already executed container of python-api and run tests with pytest:

```bash
docker-compose exec python_api pytest
```
