from abstracts.protocol import Protocol

__all__ = [
    "HTTP_Protocol"
]
class HttpBase(Protocol):
    def __init__(self, host, port) -> None:
        super().__init__(host, port)
    
    @property.getter
    def get_default_headers(self):
        return self.__default_headers
    
    def __default_headers(self):
        return (

        )