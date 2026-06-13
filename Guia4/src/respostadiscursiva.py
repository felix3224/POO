from typing import Dict, Optional
from src.resposta import Resposta


class RespostaDiscursiva(Resposta):
    def __init__(
        self,
        pergunta,
        texto_resposta: str = None,
        correction_dict: Optional[Dict] = None,
        pontuacao_obtida: float = None,
    ):
        self._texto_resposta = texto_resposta
        self._feedback = None
        self._explicacao = None

        if correction_dict:
            # Usa o resultado do LLM
            esta_correta = correction_dict.get("correta", False)
            pontuacao_obtida = correction_dict.get("pontuacao", 0.0)
            self._feedback = correction_dict.get("feedback", "")
            self._explicacao = correction_dict.get("explicacao", "")
        else:
            # Fallback: validação exata (para compatibilidade)
            esta_correta = pergunta.validar_resposta(texto_resposta)

        super().__init__(pergunta, esta_correta, pontuacao_obtida)

    def calcular_pontuacao(self) -> float:
        if self.pontuacao_obtida is not None:
            return self.pontuacao_obtida
        return 1.0 if self.esta_correta else 0.0

    def get_feedback(self) -> str:
        return self._feedback or ""
