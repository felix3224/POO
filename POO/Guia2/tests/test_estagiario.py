import pytest
from src import Estagiario


@pytest.fixture
def estagiario():
    # Salário base 1500, carga horária 30h
    return Estagiario("Carlos", "456", 1500.0, "Engenharia", 30)

# ---- Teste do bônus fixo ----
def test_bonus_fixo(estagiario):
    # 3% do salário base
    assert estagiario.calcular_bonus() == 0.03 * estagiario.salario_base

# ---- Teste do desconto fixo ----
def test_desconto_fixo(estagiario):
    # 2% do salário base
    assert estagiario.calcular_descontos() == 0.02 * estagiario.salario_base

# ---- Testes de adicionais por carga horária ----
@pytest.mark.parametrize("carga_horaria,adicional_esperado", [
    (20, 150),
    (15, 150),   # até 20h inclusive
    (25, 250),
    (30, 250),   # até 30h inclusive
    (35, 350),
    (40, 350),
])
def test_adicional_por_carga_horaria(estagiario, carga_horaria, adicional_esperado):
    estagiario.carga_horaria = carga_horaria
    assert estagiario.calcular_adicionais() == adicional_esperado

# ---- Teste de salário líquido para carga de 30h ----
def test_salario_liquido_30h(estagiario):
    estagiario.carga_horaria = 30
    # 1500 + 45 (bônus) + 250 (adicional) - 30 (desconto) = 1765
    esperado = 1500 + 45 + 250 - 30
    assert estagiario.calcular_salario_liquido() == esperado