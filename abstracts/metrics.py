from abc import ABC

class Metrics(ABC):
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data

    def __check_supported_data_type():
        pass