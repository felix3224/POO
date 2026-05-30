from src.perguntadiscursiva import PerguntaDiscursiva
from src.respostadiscursiva import RespostaDiscursiva


def criar_pergunta():
    return PerguntaDiscursiva(
        texto="O que significa CPU?",
        resposta_esperada="Central Processing Unit"
    )


def test_resposta_discursiva_correta():
    pergunta = criar_pergunta()

    resposta = RespostaDiscursiva(
        pergunta=pergunta,
        texto_resposta="Central Processing Unit"
    )

    assert resposta.esta_correta is True


def test_resposta_discursiva_errada():
    pergunta = criar_pergunta()

    resposta = RespostaDiscursiva(
        pergunta=pergunta,
        texto_resposta="Memória RAM"
    )

    assert resposta.esta_correta is False


def test_calcular_pontuacao():
    pergunta = criar_pergunta()

    resposta = RespostaDiscursiva(
        pergunta=pergunta,
        texto_resposta="Central Processing Unit"
    )

    assert resposta.calcular_pontuacao() == 1.0