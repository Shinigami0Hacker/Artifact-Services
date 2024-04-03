from abc import ABC, abstractmethod
import asyncio
from src.logs.logger import LoggerType, LoggerFactory
__all__ = [
    "Protocol"
]

class Protocol(ABC):
    def __init__(self, host, port) -> None:
        self.__host = host
        self.__port = port
        self.__logger = LoggerFactory(LoggerType.PROTOCOOL)
    def check_health_care():
        pass
    
    @abstractmethod
    async def async_send(self, data):
        """
        
        """
        raise NotImplementedError
    
    @abstractmethod
    async def run_async_group():
        """
        
        """
        raise NotImplementedError

    @abstractmethod
    def send():
        """
        
        """
        raise NotImplementedError

    @abstractmethod
    def send_all():
        """
        
        """
        raise NotImplementedError

    @abstractmethod
    def job_formatter():
        raise NotImplementedError