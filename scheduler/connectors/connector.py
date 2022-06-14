import logging
import socket
import time
import urllib.parse
from typing import Any, Callable

import requests


class Connector:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def is_host_available(self, hostname: str, port: int):
        """Check if the host is available.

        Returns:
            A boolean
        """
        try:
            socket.create_connection((hostname, port))
            return True
        except socket.error:
            return False

    def is_host_healthy(self, host: str, health_endpoint: str):
        """Check if host is healthy by inspecting the host's health endpoint.

        Returns:
            A boolean
        """
        # TODO: we can inspect the returned json to check if it is healthy
        try:
            requests.get(f"{host}{health_endpoint}")
            return True
        except requests.exceptions.RequestException:
            return False

    def retry(self, func: Callable[[], Any], *args, **kwargs) -> bool:
        """Retry a function until it returns True.

        Args:
            func: A python callable that needs to be retried.

        Returns:
            A boolean signifying whether or not the func was executed successfully.
        """
        i = 0
        while i < 10:
            if func(*args, **kwargs) is True:
                self.logger.info(
                    "Function %s, executed successfully. Retry count: %d [name=%s, args=%s, kwargs=%s]",
                    func.__name__, i, func.__name__, args, kwargs,
                )
                return True

            self.logger.warning(
                "Function %s, failed. Retry count: %d [name=%s, args=%s, kwargs=%s]",
                func.__name__, i, func.__name__, args, kwargs,
            )

            i += 1
            time.sleep(5)

        return False
