from datetime import datetime
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha
from src.perguntadiscursiva import PerguntaDiscursiva
from src.respostaobjetiva import RespostaObjetiva
from src.respostadiscursiva import RespostaDiscursiva
from src.correcao import Correcao


class TentativaQuestionario:
    def __init__(self, questionario, usuario, data_inicio=None, data_fim=None):
        self._questionario = questionario
        self._usuario = usuario
        self._data_inicio = data_inicio or datetime.now()
        self._data_fim = data_fim
        self._respostas = []
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
        elif isinstance(pergunta, PerguntaDiscursiva):
            # Usa o serviço LLM para corrigir a resposta discursiva
            correction = Correcao.corrigir_discursiva(pergunta, valor)
            resolucao = RespostaDiscursiva(
                pergunta=pergunta, texto_resposta=valor, correction_dict=correction
            )
        else:
            raise TypeError(f"Tipo de pergunta não suportado: {type(pergunta)}")

        self._respostas.append(resolucao)
        return resolucao

    def finalizar(self) -> tuple[float, str]:
        if self._finalizado:
            return self.calcular_pontuacao(), "Tentativa já finalizada."

        self._data_fim = datetime.now()
        self._finalizado = True

        pontuacao = self.calcular_pontuacao()
        total_perguntas = len(self._questionario.perguntas)
        feedback = f"Você obteve {pontuacao} de {total_perguntas} ponto(s)."
        return pontuacao, feedback

    def calcular_pontuacao(self) -> float:
        return sum(resp.calcular_pontuacao() for resp in self._respostas)

    def is_finalizado(self) -> bool:
        return self._finalizado
