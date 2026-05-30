import pytest

from src.alternativa import Alternativa


def test_criar_alternativa():
    alt = Alternativa(
        texto="Python",
        correta=True,
        explicacao="Linguagem interpretada"
    )

    assert alt.texto == "Python"
    assert alt.correta is True
    assert alt.explicacao == "Linguagem interpretada"


def test_alternativa_sem_explicacao():
    alt = Alternativa("Java", False)

    assert alt.explicacao is None