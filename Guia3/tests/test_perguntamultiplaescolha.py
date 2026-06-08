from src.alternativa import Alternativa
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha


def criar_pergunta():
    alternativas = [
        Alternativa("Java", False),
        Alternativa("Python", True),
        Alternativa("C", False),
    ]

    return PerguntaMultiplaEscolha(
        texto="Qual linguagem é interpretada?",
        alternativas=alternativas,
        explicacao_geral="Python normalmente é interpretada."
    )


def test_validar_resposta_correta():
    pergunta = criar_pergunta()

    assert pergunta.validar_resposta(1) is True


def test_validar_resposta_errada():
    pergunta = criar_pergunta()

    assert pergunta.validar_resposta(0) is False


def test_get_alternativa_correta():
    pergunta = criar_pergunta()

    correta = pergunta.get_alternativa_correta()

    assert correta.texto == "Python"
    assert correta.correta is True


def test_get_tipo():
    pergunta = criar_pergunta()

    assert pergunta.get_tipo() == "multipla_escolha"


def test_get_explicacao():
    pergunta = criar_pergunta()

    assert pergunta.get_explicacao() == (
        "Python normalmente é interpretada."
    )