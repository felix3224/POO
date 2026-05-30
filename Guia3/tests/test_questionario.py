import pytest

from src.questionario import Questionario
from src.perguntadiscursiva import PerguntaDiscursiva
from src.tentativaquestionario import TentativaQuestionario


def test_adicionar_pergunta():
    questionario = Questionario("Quiz POO")

    pergunta = PerguntaDiscursiva(
        texto="O que é encapsulamento?"
    )

    questionario.adicionar_pergunta(pergunta)

    assert len(questionario.perguntas) == 1


def test_criar_attempt():
    questionario = Questionario("Quiz Redes")

    tentativa = questionario.criar_attempt("valter")

    assert isinstance(tentativa, TentativaQuestionario)
    assert tentativa.usuario == "valter"

