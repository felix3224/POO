from correcao import Correcao
from perguntadiscursiva import PerguntaDiscursiva

p = PerguntaDiscursiva("O que é Python?", "Linguagem de programação interpretada")
result = Correcao.corrigir_discursiva(p, "Python é uma linguagem interpretada")
print(result)
