from typing import List, Tuple, Dict


class Alternativa:  # it mean that might to be String or nada
    def __init__(self, texto: str, correta: bool, explicacao: str = None):
        self.texto = texto
        self.correta = correta
        self.explicacao = explicacao
