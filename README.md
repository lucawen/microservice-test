# Microservices

A microservice that make a request to another microservice and store their data into storage for caching

- API A: python-service
- API B: rust-service

I made the rust-service like a service made from another person, like if i don't know very well

The api A request api B and store the value from api B into databases in the layer of api A. If already have a request to something that already has processed, will return the cached value from the database

## Documentation

The documentation for python-service (api A) its located under /docs on 127.0.0.1:8000

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
