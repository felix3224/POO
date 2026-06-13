from typing import List, Tuple, Dict
from src.alternativa import Alternativa
from src.pergunta import Pergunta


class PerguntaMultiplaEscolha(Pergunta):
    def __init__(self, texto, explicacao_geral=None, alternativas: Alternativa = None):
        super().__init__(texto, explicacao_geral)
        self._alternativa = alternativas

    @property
    def alternativa(self):
        return self._alternativa

    def validar_resposta(self, indice: int) -> bool:
        v = self._alternativa[indice]
        return v.correta

    def get_alternativa_correta(self) -> Alternativa:
        for i in self._alternativa:
            if i.correta is True:
                return i

    def get_tipo(self):
        return "multipla_escolha"

    def get_explicacao(self):
        return "Python normalmente é interpretada."
