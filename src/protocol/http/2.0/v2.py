from abstracts.protocol import Protocol
from src.protocol.http_protocol.base import HttpBase
import httplib2
class HttpV2Connection(HttpBase):
    def __init__(self, host, port, header = None) -> None:
        super().__init__(host, port)
        self.header = header or self.get_default_headers
