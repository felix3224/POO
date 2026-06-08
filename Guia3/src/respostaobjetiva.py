from typing import List, Tuple, Dict
from resposta import Resposta
from alternativa import Alternativa


class RespostaObjetiva(Resposta):
    def __init__(
        self,
        pergunta,
        esta_correta,
        pontuacao_obtida,
        indice_escolhido: int,
        alternativa_selecionada: Alternativa = None,
    ):
        super().__init__(pergunta, esta_correta, pontuacao_obtida)
        self.__indice_escolhido = indice_escolhido
        self.__alternativa_selecionada = alternativa_selecionada
