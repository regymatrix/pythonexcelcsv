from abc import ABC, abstractmethod

class RegraStrategy(ABC):
    @abstractmethod
    def aplicar(self, dados):
        pass
