from typing import List, Tuple, Dict
from abc import ABC, abstractmethod


class Pergunta(ABC):
    def __init__(self, texto: str, explicacao_geral: str = None):
        self._texto = texto
        self._explicacao_geral = explicacao_geral

    @property
    def texto(self):
        return self._texto

    @abstractmethod
    def validar_resposta(self, resposta) -> bool:
        pass

    def get_explicacao(self) -> str:
        return self._explicacao_geral

    def get_tipo(self) -> str:
        pass
