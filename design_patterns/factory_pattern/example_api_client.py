from abc import ABC, abstractmethod
from typing import Dict, Any


class APIClient(ABC):
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    @abstractmethod
    def get(self, endpoint: str):
        pass

    @abstractmethod
    def post(self, endpoint: str, data: Dict[str, Any]):
        pass


class RESTClient(APIClient):
    def get(self, endpoint: str):
        return f"REST GET: {self.base_url}/{endpoint} " \
            f"with key {self.api_key[:5]}..."

    def post(self, endpoint: str, data: Dict[str, Any]):
        return f"REST POST: {self.base_url}/{endpoint} with data: {data}"


class GraphQLClient(APIClient):
    def get(self, endpoint: str):
        return f"GraphQL Query: {self.base_url} - {endpoint}"

    def post(self, endpoint: str, data: Dict[str, Any]):
        return f"GraphQL Mutation: {self.base_url} with variables: {data}"


class SOAPClient(APIClient):
    def get(self, endpoint: str):
        return f"SOAP Request: {self.base_url} - {endpoint}"

    def post(self, endpoint: str, data: Dict[str, Any]):
        return f"SOAP Call: {self.base_url} with envelope: {data}"


class APIClientFactory:
    _clients = {
            'rest': RESTClient,
            'graphql': GraphQLClient,
            'soap': SOAPClient
    }

    @classmethod
    def create_client(cls, client_type: str, base_url: str, api_key: str):
        client_class = cls._clients.get(client_type.lower())
        if not client_class:
            raise ValueError(f"Unsupported API client type: {client_type}")
        return client_class(base_url, api_key)


# Usage
rest_client = APIClientFactory.create_client(
    'rest', 'https://api.example.com', 'abc123')
print(rest_client.get('users'))
print(rest_client.post('users', {'name': 'John', 'email': 'john@example.com'}))

graphql_client = APIClientFactory.create_client(
    'graphql', 'https://api.graphql.com', 'xyz789')
print(graphql_client.get('{ users { name email } }'))
