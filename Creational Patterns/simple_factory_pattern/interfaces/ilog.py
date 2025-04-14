from abc import ABC, abstractmethod

# Abstract base class for loggers
class ILog(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass
