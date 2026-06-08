from typing import List, Tuple, Dict
from abc import ABC, abstractmethod


class Resposta(ABC):
    def __init__(self, pergunta, esta_correta, pontuacao_obtida):
        self.__pergunta = pergunta
        self.__esta_correta = esta_correta
        self.__pontuacao_obtida = pontuacao_obtida

    @abstractmethod
    def calcular_pontuacao(self) -> float:
        pass
