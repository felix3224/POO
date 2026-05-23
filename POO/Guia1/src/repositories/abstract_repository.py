from abc import ABC, abstractmethod

class AbstractRepository(ABC):

    @abstractmethod
    def load_all(self):
        pass

    @abstractmethod
    def search(self, term: str):
        pass