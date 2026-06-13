from typing import List, Tuple, Dict
from abc import ABC, abstractmethod
from src.pergunta import Pergunta


class Resposta(ABC):
    def __init__(
        self,
        pergunta: Pergunta,
        esta_correta: bool = False,
        pontuacao_obtida: float = None,
    ):
        self.pergunta = pergunta
        self.esta_correta = esta_correta
        self.pontuacao_obtida = pontuacao_obtida

    @abstractmethod
    def calcular_pontuacao(self) -> float:
        pass
