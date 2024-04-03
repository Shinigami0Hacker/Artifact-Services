import requests
import asyncio
from abstracts.protocol import Protocol
from src.protocol.http_protocol.base import HttpBase
from typing import overload

class HttpV1Connection(HttpBase):
    def __init__(self, host, port, header = None) -> None:
        super().__init__(host, port)
        self.header = header or self.get_default_headers
    
    @overload
    async def async_send(self, data):
        pass

    @overload
    async def __async_send_all(self, jobs):
        with asyncio.TaskGroup() as group:
            asyncio.create_task()

    @overload
    async def async_send_all(self):
        return asyncio.to_thread(self.async_send_all)
    