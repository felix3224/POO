from typing import List, Tuple, Dict
from src.resposta import Resposta
from src.alternativa import Alternativa
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha


class RespostaObjetiva(Resposta):
    def __init__(
        self,
        pergunta: PerguntaMultiplaEscolha,
        indice_escolhido: int = None,
        alternativa_selecionada: Alternativa = None,
    ):
        self._indice_escolhido = indice_escolhido
        self._alternativa_selecionada = alternativa_selecionada

        esta_correta = pergunta.validar_resposta(self._indice_escolhido)
        super().__init__(pergunta, esta_correta)

    def calcular_pontuacao(self):
        if self.esta_correta:
            return 1.0
        else:
            return 0
