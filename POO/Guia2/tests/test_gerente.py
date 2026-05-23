import pytest
from src import Gerente


@pytest.fixture
def gerente():
    # Salário base 8000, equipe = 5 (para teste básico)
    return Gerente("Roberta", "789", 8000.0, "TI", 5)

# ---- Testes de bônus por tamanho da equipe ----
@pytest.mark.parametrize("qtd_equipe,percentual_bonus", [
    (3, 0.10),
    (5, 0.10),
    (6, 0.15),
    (10, 0.15),
    (11, 0.20),
    (20, 0.20),
])
def test_bonus_por_tamanho_equipe(gerente, qtd_equipe, percentual_bonus):
    gerente.qtd_equipe = qtd_equipe
    esperado = percentual_bonus * gerente.salario_base
    assert gerente.calcular_bonus() == esperado

# ---- Teste de desconto fixo ----
def test_desconto_fixo(gerente):
    # 12% do salário base
    assert gerente.calcular_descontos() == 0.12 * gerente.salario_base

# ---- Testes de adicional por tamanho da equipe ----
@pytest.mark.parametrize("qtd_equipe,adicional_esperado", [
    (1, 500),
    (5, 500),
    (6, 1000),
    (10, 1000),
    (11, 2000),
    (15, 2000),
])
def test_adicional_por_tamanho_equipe(gerente, qtd_equipe, adicional_esperado):
    gerente.qtd_equipe = qtd_equipe
    assert gerente.calcular_adicionais() == adicional_esperado

# ---- Teste integrado para equipe de 8 pessoas ----
def test_salario_liquido_equipe_8(gerente):
    gerente.qtd_equipe = 8
    # bonus 15% = 1200, adicional = 1000, desconto 12% = 960
    esperado = 8000 + 1200 + 1000 - 960  # 9240
    assert gerente.calcular_salario_liquido() == esperado