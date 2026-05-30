from src.alternativa import Alternativa
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha
from src.perguntadiscursiva import PerguntaDiscursiva
from src.questionario import Questionario
from src.tentativaquestionario import TentativaQuestionario


def criar_questionario():
    q = Questionario("Quiz")

    p1 = PerguntaMultiplaEscolha(
        texto="2 + 2?",
        alternativas=[
            Alternativa("3", False),
            Alternativa("4", True),
        ]
    )

    p2 = PerguntaDiscursiva(
        texto="Sigla CPU",
        resposta_esperada="Central Processing Unit"
    )

    q.adicionar_pergunta(p1)
    q.adicionar_pergunta(p2)

    return q


def test_registrar_resposta_objetiva():
    q = criar_questionario()

    tentativa = TentativaQuestionario(
        questionario=q,
        usuario="valter"
    )

    tentativa.registrar_resposta(0, 1)

    assert len(tentativa.respostas) == 1


def test_registrar_resposta_discursiva():
    q = criar_questionario()

    tentativa = TentativaQuestionario(
        questionario=q,
        usuario="valter"
    )

    tentativa.registrar_resposta(
        1,
        "Central Processing Unit"
    )

    assert len(tentativa.respostas) == 1


def test_calcular_pontuacao():
    q = criar_questionario()

    tentativa = TentativaQuestionario(
        questionario=q,
        usuario="valter"
    )

    tentativa.registrar_resposta(0, 1)
    tentativa.registrar_resposta(
        1,
        "Central Processing Unit"
    )

    assert tentativa.calcular_pontuacao() == 2.0


def test_finalizar():
    q = criar_questionario()

    tentativa = TentativaQuestionario(
        questionario=q,
        usuario="valter"
    )

    tentativa.registrar_resposta(0, 1)

    pontuacao, feedback = tentativa.finalizar()

    assert pontuacao >= 0
    assert isinstance(feedback, str)
    assert tentativa.is_finalizado() is True