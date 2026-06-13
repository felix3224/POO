from typing import Dict
from perguntadiscursiva import PerguntaDiscursiva
from llmservice import LLMService


class Correcao:
    @staticmethod
    def corrigir_discursiva(
        pergunta: PerguntaDiscursiva, resposta_aluno: str, service: LLMService = None
    ) -> Dict:
        if service is None:
            service = LLMService()
        return service.corrigir_resposta(pergunta, resposta_aluno)

    @staticmethod
    def criar_prompt_correcao(pergunta: PerguntaDiscursiva, resposta_aluno: str) -> str:
        # Método utilitário para visualizar/gerar o prompt sem chamar a API
        texto_pergunta = pergunta.texto
        resposta_esperada = pergunta.resposta_esperada or "Não informada"
        return f"""
Pergunta: {texto_pergunta}
Resposta esperada: {resposta_esperada}
Resposta do aluno: {resposta_aluno}
"""
