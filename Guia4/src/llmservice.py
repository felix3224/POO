import os
import json
from typing import Dict
from groq import Groq
from .perguntadiscursiva import PerguntaDiscursiva


class LLMService:
    def __init__(self, api_key: str = None, model: str = "llama-3.3-70b-versatile"):
        self.api_key = api_key or os.environ.get("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key não fornecida. Defina GROQ_API_KEY ou passe o argumento."
            )
        self.model = model
        self.client = Groq(api_key=self.api_key)

    def corrigir_resposta(
        self, pergunta: PerguntaDiscursiva, resposta_aluno: str
    ) -> Dict:
        prompt = self._montar_prompt(pergunta, resposta_aluno)
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                response_format={"type": "json_object"},
            )
            resposta_raw = response.choices[0].message.content
            resultado = json.loads(resposta_raw)
            if not all(
                k in resultado
                for k in ("correta", "pontuacao", "feedback", "explicacao")
            ):
                raise ValueError(
                    "Resposta da API não contém todos os campos necessários."
                )
            return resultado
        except Exception as e:
            return {
                "correta": False,
                "pontuacao": 0.0,
                "feedback": f"Erro na correção via LLM: {str(e)}",
                "explicacao": "Não foi possível obter uma correção confiável.",
            }

    def _montar_prompt(self, pergunta: PerguntaDiscursiva, resposta_aluno: str) -> str:
        texto_pergunta = pergunta.texto
        resposta_esperada = pergunta.resposta_esperada or "Não informada"
        return f"""
Você é um corretor de questões discursivas.

Pergunta: {texto_pergunta}

Resposta esperada (referência): {resposta_esperada}

Resposta do aluno: {resposta_aluno}

Analise se a resposta do aluno está **substancialmente correta** considerando o esperado.
Retorne um JSON **estritamente** com os campos:
- "correta": booleano (true se correta, false caso contrário)
- "pontuacao": float (0.0 ou 1.0, pois a pergunta vale 1 ponto)
- "feedback": string (um breve comentário para o aluno)
- "explicacao": string (justificativa da correção)

Não inclua texto adicional fora do JSON.
"""
