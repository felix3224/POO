import os
from dotenv import load_dotenv
from src.perguntadiscursiva import PerguntaDiscursiva
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha
from src.alternativa import Alternativa
from src.questionario import Questionario

load_dotenv()

# Configure a chave da API (idealmente via variável de ambiente)

# Criação do questionário
quiz = Questionario("Avaliação de Python")

# Pergunta de múltipla escolha
alt1 = Alternativa("Compilada", False, "Python é interpretada.")
alt2 = Alternativa(
    "Interpretada", True, "Correto! Python é uma linguagem interpretada."
)
mult = PerguntaMultiplaEscolha(
    texto="Qual a natureza da linguagem Python?",
    explicacao_geral="Python é interpretada, não compilada.",
    alternativas=[alt1, alt2],
)
quiz.adicionar_pergunta(mult)

# Pergunta discursiva
disc = PerguntaDiscursiva(
    texto="Explique o que é um dicionário em Python.",
    resposta_esperada="É uma estrutura de dados que armazena pares chave-valor.",
)
quiz.adicionar_pergunta(disc)

# Simulação de tentativa
tentativa = quiz.criar_attempt("aluno@email.com")

# Respostas
tentativa.registrar_resposta(0, 1)  # índice 1 é a alternativa correta
tentativa.registrar_resposta(
    1, "Dicionário é uma coleção de pares chave-valor, mutável."
)

# Finaliza e mostra resultado
pontos, feedback = tentativa.finalizar()
print(feedback)
print(f"Pontuação final: {pontos}")

# Exibe detalhes da correção da discursiva (feedback do LLM)
resposta_disc = tentativa.respostas[1]
if hasattr(resposta_disc, "get_feedback"):
    print(f"Feedback do LLM: {resposta_disc.get_feedback()}")
