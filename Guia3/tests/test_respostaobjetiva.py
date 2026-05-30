from src.alternativa import Alternativa
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha
from src.respostaobjetiva import RespostaObjetiva


def criar_pergunta():
    alternativas = [
        Alternativa("HTTP", False),
        Alternativa("TCP/IP", True),
    ]

    return PerguntaMultiplaEscolha(
        texto="Qual protocolo é base da internet?",
        alternativas=alternativas
    )


def test_resposta_objetiva_correta():
    pergunta = criar_pergunta()

    resposta = RespostaObjetiva(
        pergunta=pergunta,
        indice_escolhido=1
    )

    assert resposta.esta_correta is True


def test_resposta_objetiva_errada():
    pergunta = criar_pergunta()

    resposta = RespostaObjetiva(
        pergunta=pergunta,
        indice_escolhido=0
    )

    assert resposta.esta_correta is False


def test_calcular_pontuacao_correta():
    pergunta = criar_pergunta()

    resposta = RespostaObjetiva(
        pergunta=pergunta,
        indice_escolhido=1
    )

    assert resposta.calcular_pontuacao() == 1.0


def test_calcular_pontuacao_errada():
    pergunta = criar_pergunta()

    resposta = RespostaObjetiva(
        pergunta=pergunta,
        indice_escolhido=0
    )

    assert resposta.calcular_pontuacao() == 0.0