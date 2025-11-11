import os
import requests
from urllib.parse import urljoin

DEFAULT_SERVER = os.environ.get('ZYX_SERVER', 'http://localhost:8081')

class HttpClient:
    def __init__(self, server_url=None, user=None, password=None, token=None, timeout=10):
        self.base = (server_url or os.environ.get('ZYX_SERVER') or DEFAULT_SERVER).rstrip('/') + '/'
        self.timeout = timeout
        self.token = token or os.environ.get('ZYX_TOKEN')
        self.user = user or os.environ.get('ZYX_USER')
        self.password = password or os.environ.get('ZYX_PASS')

    def _headers(self):
        h = {}
        if self.token:
            h['Authorization'] = f'Bearer {self.token}'
        return h

    def _auth(self):
        if self.user and self.password:
            return (self.user, self.password)
        return None

    def get(self, path, params=None):
        url = urljoin(self.base, path.lstrip('/'))
        return requests.get(url, params=params, headers=self._headers(), auth=self._auth(), timeout=self.timeout)

    def post(self, path, params=None, json=None):
        url = urljoin(self.base, path.lstrip('/'))
        return requests.post(url, params=params, json=json, headers=self._headers(), auth=self._auth(), timeout=self.timeout)

    def put(self, path, params=None, json=None):
        url = urljoin(self.base, path.lstrip('/'))
        return requests.put(url, params=params, json=json, headers=self._headers(), auth=self._auth(), timeout=self.timeout)

    def delete(self, path, params=None):
        url = urljoin(self.base, path.lstrip('/'))
        return requests.delete(url, params=params, headers=self._headers(), auth=self._auth(), timeout=self.timeout)
