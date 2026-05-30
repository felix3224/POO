import pytest

from src.resposta import Resposta


def test_nao_instanciar_resposta_abstract():
    with pytest.raises(TypeError):
        Resposta(None)