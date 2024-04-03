import logging
from enum import Enum

class LoggerType(Enum):
    THREAD = 0
    PROTOCOOL = 1
    def type_exception():
        print("")
        print(f"{'The avaible type are':_^25}")
        for i, logger_type in enumerate(LoggerType.name): 
            print(f"{i}. {logger_type}")

class LoggerFactory():
    def __init__(self, type) -> None:
        pass
    def __standard_logger(self):
        logger = logging.Logger()

    def create_logger(self, logger_type):
        assert isinstance(logger_type, LoggerType), LoggerType.type_exception()

        match logger_type:
            case LoggerType.THREAD:
                pass
            case LoggerType.PROTOCOOL:
                pass
            case _:
                return self.__standard_logger()