import os
from dotenv import load_dotenv
from src.perguntadiscursiva import PerguntaDiscursiva
from src.perguntamultiplaescolha import PerguntaMultiplaEscolha
from src.alternativa import Alternativa
from src.questionario import Questionario


def main():
    # Carrega as variáveis de ambiente
    load_dotenv()

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
        1, "Dicionário é uma coleção de pares chave-valor, mutável.\n"
    )

    # Finaliza e mostra resultado
    pontos, feedback = tentativa.finalizar()

    print("\n--- Detalhes das respostas ---")
    for resp in tentativa.respostas:
        print(resp.descrever())
        print("-" * 40)

    print(feedback)
    print(f"Pontuação final: {pontos}")


if __name__ == "__main__":
    main()
