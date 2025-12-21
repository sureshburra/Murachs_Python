import requests


class HttpRequestBuilder:
    def __init__(self):
        self._method = "GET"
        self._url = None
        self._headers = {}
        self._params = {}
        self._json = None
        self._timeout = 10

    def method(self, method):
        self._method = method.upper()
        return self

    def url(self, url):
        self._url = url
        return self

    def header(self, key, value):
        self._headers[key] = value
        return self

    def param(self, key, value):
        self._params[key] = value
        return self

    def json_body(self, data):
        self._json = data
        return self

    def timeout(self, timeout):
        self._timeout = timeout
        return self

    def send(self):
        if not self._url:
            raise ValueError("URL is required")
        return requests.request(
            method=self._method,
            url=self._url,
            headers=self._headers,
            params=self._params,
            json=self._json,
            timeout=self._timeout,
        )


# Usage
response = (
    HttpRequestBuilder()
    .method("post")
    .url("https://api.example.com/items")
    .header("Authorization", "Bearer TOKEN")
    .json_body({"name": "item1"})
    .timeout(5)
    .send()
)
