import pytest

from src.pergunta import Pergunta


def test_nao_instanciar_pergunta_abstract():
    with pytest.raises(TypeError):
        Pergunta("Pergunta abstrata")