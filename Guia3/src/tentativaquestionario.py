from typing import List, Tuple, Dict
from resposta import Resposta
from datetime import datetime


class TentativaQuestionario:
    def __init__(
        self, questionario=None, usuario=None, data_inicio=None, data_fim=None
    ):
        self._questionario = questionario
        self._usuario = usuario
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self.respostas = []  # for Class Resposta

    def registrar_resposta(self, indice_pergunta, valor):
        pass

    def finalizar(self) -> tuple[float, str]:
        pass

    def calcular_pontuacao(self) -> float:
        pass

    def is_finalizado(self) -> bool:
        pass
