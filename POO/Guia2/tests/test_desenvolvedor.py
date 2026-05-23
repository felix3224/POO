import pytest
from src import Desenvolvedor


@pytest.fixture
def desenvolvedor():
    # Instância base com salário 5000, linguagem Python, senioridade pleno
    return Desenvolvedor("Ana", "123", 5000.0, "Python", "pleno")

# ---- Testes para calcular_bonus() ----
@pytest.mark.parametrize("senioridade,percentual", [
    ("junior", 0.05),
    ("pleno", 0.10),
    ("senior", 0.15),
])
def test_bonus_por_senioridade(desenvolvedor, senioridade, percentual):
    desenvolvedor.senioridade = senioridade
    esperado = percentual * desenvolvedor.salario_base
    assert desenvolvedor.calcular_bonus() == esperado

# ---- Teste para calcular_descontos() ----
def test_desconto_fixo(desenvolvedor):
    # 8% do salário base
    assert desenvolvedor.calcular_descontos() == 0.08 * desenvolvedor.salario_base

# ---- Testes para calcular_adicionais() ----
@pytest.mark.parametrize("linguagem,adicional_esperado", [
    ("Python", 500),
    ("Java", 400),
    ("JavaScript", 350),
    ("C++", 200),
    ("Ruby", 200),
])
def test_adicional_por_linguagem(desenvolvedor, linguagem, adicional_esperado):
    desenvolvedor.linguagem = linguagem
    assert desenvolvedor.calcular_adicionais() == adicional_esperado

# ---- Teste integrado de salário líquido ----
def test_salario_liquido_pleno_python(desenvolvedor):
    desenvolvedor.senioridade = "pleno"
    desenvolvedor.linguagem = "Python"
    # salario_base (5000) + bonus(10%) + adicional(500) - desconto(8%)
    esperado = 5000 + 500 + 500 - 400  # 5600
    assert desenvolvedor.calcular_salario_liquido() == esperado