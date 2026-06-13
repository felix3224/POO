from typing import List
from src.alternativa import Alternativa
from src.pergunta import Pergunta


class PerguntaMultiplaEscolha(Pergunta):
    def __init__(
        self, texto, explicacao_geral=None, alternativas: List[Alternativa] = None
    ):
        super().__init__(texto, explicacao_geral)
        self._alternativas = alternativas or []

    @property
    def alternativas(self):
        return self._alternativas

    def validar_resposta(self, indice: int) -> bool:
        if 0 <= indice < len(self._alternativas):
            return self._alternativas[indice].correta
        return False

    def get_alternativa_correta(self) -> Alternativa:
        for alt in self._alternativas:
            if alt.correta:
                return alt
        return None

    def get_tipo(self):
        return "multipla_escolha"

    def get_explicacao(self):
        return self._explicacao_geral or "Sem explicação adicional."
