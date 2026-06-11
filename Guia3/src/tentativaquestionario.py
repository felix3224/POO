from typing import List, Tuple, Dict
from datetime import datetime

from src.perguntamultiplaescolha import PerguntaMultiplaEscolha

from src.respostaobjetiva import RespostaObjetiva
from src.respostadiscursiva import RespostaDiscursiva


class TentativaQuestionario:
    def __init__(self, questionario, usuario, data_inicio=None, data_fim=None):
        self._questionario = questionario
        self._usuario = usuario
        self._data_inicio = data_inicio or datetime.now()
        self._data_fim = data_fim
        self._respostas = []  # for Class Resposta
        self._finalizado = False

    @property
    def respostas(self):
        return self._respostas

    @property
    def usuario(self):
        return self._usuario

    def registrar_resposta(self, indice_pergunta, valor):
        pergunta = self._questionario.perguntas[indice_pergunta]

        if isinstance(pergunta, PerguntaMultiplaEscolha):
            resolucao = RespostaObjetiva(pergunta=pergunta, indice_escolhido=valor)
        else:
            resolucao = RespostaDiscursiva(pergunta=pergunta, texto_resposta=valor)

        self._respostas.append(resolucao)
        return resolucao

    def finalizar(self) -> tuple[float, str]:
        # Finaliza a tentativa, calcula pontuação e gera feedback.
        if self._finalizado:
            return self.calcular_pontuacao(), "Tentativa já finalizada."

        self._data_fim = datetime.now()
        self._finalizado = True

        pontuacao = self.calcular_pontuacao()
        total_perguntas = len(self._questionario.perguntas)
        feedback = f"Você obteve {pontuacao} de {total_perguntas} ponto(s)."

        return pontuacao, feedback

    def calcular_pontuacao(self) -> float:
        total = 0.0
        for resposta in self._respostas:
            total += resposta.calcular_pontuacao()
        return total

    def is_finalizado(self) -> bool:
        return True
