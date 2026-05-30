from src.perguntadiscursiva import PerguntaDiscursiva


def test_validar_resposta_correta():
    pergunta = PerguntaDiscursiva(
        texto="O que é POO?",
        resposta_esperada="Programação Orientada a Objetos"
    )

    resposta = "Programação Orientada a Objetos"

    assert pergunta.validar_resposta(resposta) is True


def test_validar_resposta_errada():
    pergunta = PerguntaDiscursiva(
        texto="O que é POO?",
        resposta_esperada="Programação Orientada a Objetos"
    )

    resposta = "Banco de dados"

    assert pergunta.validar_resposta(resposta) is False


def test_pergunta_sem_resposta_esperada():
    pergunta = PerguntaDiscursiva(
        texto="Explique encapsulamento."
    )

    assert pergunta.resposta_esperada is None


def test_get_tipo():
    pergunta = PerguntaDiscursiva(
        texto="Explique herança."
    )

    assert pergunta.get_tipo() == "discursiva"