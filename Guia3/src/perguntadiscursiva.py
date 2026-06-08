from typing import List, Tuple, Dict
from src.pergunta import Pergunta


class PerguntaDiscursiva(Pergunta):
    def __init__(
        self,
        texto,
        resposta_esperada=None,
        explicacao_geral: str = None,
        case_sensitive: bool = False,
    ):
        super().__init__(texto, explicacao_geral)
        self._resposta_esperada = resposta_esperada
        self._case_sensitive = case_sensitive

    @property
    def resposta_esperada(self):
        return self._resposta_esperada

    def validar_resposta(self, texto: str) -> bool:

        if self._resposta_esperada is None:
            return

        if not self._case_sensitive:
            return self._resposta_esperada.lower() == texto.lower()

        return self._resposta_esperada == texto

    def get_tipo(self):
        return "discursiva"
