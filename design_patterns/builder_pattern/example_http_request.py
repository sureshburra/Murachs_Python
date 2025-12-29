# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 08:03:46 2025

@author: suresh.burra
"""
from typing import Dict, Optional, Any
from enum import Enum

class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    
    
class HTTPRequest:
    def __init__(self):
        self.method: Optional[HTTPMethod] = None
        self.url: Optional[str] = None
        self.headers: Dict[str, str] = {}
        self.query_params: Dict[str, str] = {}
        self.body: Optional[Any] = None
        self.timeout: int = 30
        self.auth: Optional[tuple] = None
        
    def __str__(self):
        query_string = "&".join([f"{k}={v}" for k,v in self.query_params.items()])
        full_url = f"{self.url}?{query_string}" if query_string else self.url
        
        return (f"HTTP Request:\n"
                f"Method: {self.method.value if self.method else 'None'}\n"
                f"URL: {full_url}\n"
                f"Headers: {self.headers}\n"
                f"Body: {self.body}\n"
                f"Timeout: {self.timeout}s"
                )
    
    
class HTTPRequestBuilder:
    def __init__(self):
        self.request = HTTPRequest()
        
    def set_method(self, method: HTTPMethod):
        self.request.method = method
        return self
    
    def get(self, url: str):
        self.request.method = HTTPMethod.GET
        self.request.url = url
        return self
    
    def post(self, url: str):
        self.request.method = HTTPMethod.POST
        self.request.url = url
        return self
    
    def put(self, url: str):
        self.request.method = HTTPMethod.PUT
        self.request.url = url
        return self
    
    def delete(self, url: str):
        self.request.method = HTTPMethod.DELETE
        self.request.url = url
        return self
    
    def add_header(self, key: str,value: str):
        self.request.headers[key] = value
        return self
    
    def add_headers(self, headers: Dict[str, str]):
        self.request.headers.update(headers)
        return self
    
    def add_query_param(self, key: str, value: str):
        self.request.query_params[key] = value
        return self
    
    def add_query_params(self, params: Dict[str, str]):
        self.request.query_params.update(params)
        return self
    
    def set_body(self, body: Any):
        self.request.body = body
        return self
    
    def set_json_body(self, data: Dict):
        self.request.body = data
        self.add_header("Content-Type", "application/json")
        return self
    
    def set_timeout(self, timeout: int):
        self.request.timeout = timeout
        return self
    
    def set_auth(self, username: str, password: str):
        self.request.auth = (username, password)
        return self
    
    def build(self):
        if not self.request.url:
            raise ValueError("URL must be specified")
        if not self.request.method:
            raise ValueError("HTTP method must be specified")
        return self.request
    

# Usage
request = (HTTPRequestBuilder()
           .post("https://api.example.com/users")
           .add_headers({
               "Authorization": "Bearer token123",
               "Accept": "application/json"
               })
           .add_query_param("include", "profile")
           .set_json_body({"name": "John Doe", "email": "john@example.com"})
           .set_timeout(60)
           .build()           
           )

print(request)
