import logging

import requests
import logging


class APIBase:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def get_method(self, url, headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        response = requests.request("GET", url, headers=headers, data=payload)
        self.log.info(f"URL: {url}")
        self.log.info(f"Headers: {headers}")
        self.log.info(f"Payload: {payload}")
        self.log.info(f"Response: {response.json()}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code

    def post_method(self, url, headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        response = requests.request("POST", url, headers=headers, data=payload)
        self.log.info(f"URL: {url}")
        self.log.info(f"Headers: {headers}")
        self.log.info(f"Payload: {payload}")
        self.log.info(f"Response: {response.json()}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code

    def put_method(self, url, headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        response = requests.request("PUT", url, headers=headers, data=payload)
        self.log.info(f"URL: {url}")
        self.log.info(f"Headers: {headers}")
        self.log.info(f"Payload: {payload}")
        self.log.info(f"Response: {response.json()}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code

    def patch_method(self, url, headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        response = requests.request("PATCH", url, headers=headers, data=payload)
        self.log.info(f"URL: {url}")
        self.log.info(f"Headers: {headers}")
        self.log.info(f"Payload: {payload}")
        self.log.info(f"Response: {response.json()}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code

    def delete_method(self, url, headers=None, payload=None):
        headers = headers if headers is not None else {}
        payload = payload if payload is not None else {}
        response = requests.request("DELETE", url, headers=headers, data=payload)
        self.log.info(f"URL: {url}")
        self.log.info(f"Headers: {headers}")
        self.log.info(f"Payload: {payload}")
        self.log.info(f"Response: {response.json()}")
        self.log.info(f"status code: {response.status_code}")
        return response.json(), response.status_code
