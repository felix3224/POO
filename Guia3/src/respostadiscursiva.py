from typing import List, Tuple, Dict
from resposta import Resposta


class RespostaDiscursiva(Resposta):
    def __init__(self, pergunta, esta_correta, pontuacao_obtida, texto_resposta: str):
        super().__init__(pergunta, esta_correta, pontuacao_obtida)
        self.__texto_resposta = texto_resposta
