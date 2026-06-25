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

        if alternativa_selecionada is None and indice_escolhido is not None:
            alternativas = pergunta.alternativas
            if 0 <= indice_escolhido < len(alternativas):
                alternativa_selecionada = alternativas[indice_escolhido]
        self._alternativa_selecionada = alternativa_selecionada

        esta_correta = pergunta.validar_resposta(self._indice_escolhido)
        super().__init__(pergunta, esta_correta)

    def calcular_pontuacao(self):
        if self.esta_correta:
            return 1.0
        else:
            return 0

    def descrever(self) -> str:
        if self._alternativa_selecionada is not None:
            texto_escolhido = self._alternativa_selecionada.texto
        else:
            texto_escolhido = "Nenhuma alternativa selecionada"

        status = "Correta" if self.esta_correta else "Incorreta"
        linhas = [
            f"Pergunta: {self.pergunta.texto}",
            f"Resposta dada: {texto_escolhido} ({status})",
        ]

        if not self.esta_correta:
            alt_correta = self.pergunta.get_alternativa_correta()
            if alt_correta is not None:
                linhas.append(f"Resposta correta: {alt_correta.texto}")
            explicacao = self.pergunta.get_explicacao()
            if explicacao:
                linhas.append(f"Explicação: {explicacao}")

        return "\n".join(linhas)
