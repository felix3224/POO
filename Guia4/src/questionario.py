from typing import List, Tuple, Dict
from src.pergunta import Pergunta
from src.tentativaquestionario import TentativaQuestionario


class Questionario:
    def __init__(self, titulo: str):
        self._titulo = titulo
        self._perguntas = []

    @property
    def titulo(self):
        return self._titulo

    @property
    def perguntas(self):
        return self._perguntas

    def adicionar_pergunta(self, p: Pergunta):
        self._perguntas.append(p)

    def criar_attempt(self, usuario: str) -> TentativaQuestionario:
        t = TentativaQuestionario(questionario=self, usuario=usuario)
        return t
