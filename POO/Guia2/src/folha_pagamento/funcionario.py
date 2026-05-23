from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, matricula: str, salario_base: float):
        if not nome:
            raise ValueError("Nome inválido.")

        if not matricula:
            raise ValueError("Matrícula inválida.")

        if salario_base < 0:
            raise ValueError("Salário não pode ser negativo.")

        self._nome = nome
        self._matricula = matricula
        self._salario_base = salario_base

    # ---------------------------
    # Propriedades comuns
    # ---------------------------
    @property
    def nome(self) -> str:
        return self._nome

    @property
    def matricula(self) -> str:
        return self._matricula

    @property
    def salario_base(self) -> float:
        return self._salario_base

    # ---------------------------
    # Métodos concretos
    # ---------------------------
    def dados_basicos(self) -> dict:
        return {
            "nome": self.nome,
            "matricula": self.matricula,
            "salario_base": self.salario_base,
            "cargo": self.__class__.__name__
        }

    def calcular_salario_liquido(self) -> float:
        return (
            self.salario_base
            + self.calcular_bonus()
            + self.calcular_adicionais()
            - self.calcular_descontos()
        )

    def gerar_contracheque(self) -> dict:
        return {
            "nome": self.nome,
            "matricula": self.matricula,
            "cargo": self.__class__.__name__,
            "salario_base": self.salario_base,
            "bonus": self.calcular_bonus(),
            "adicionais": self.calcular_adicionais(),
            "descontos": self.calcular_descontos(),
            "salario_liquido": self.calcular_salario_liquido()
        }

    # ---------------------------
    # Contrato abstrato
    # ---------------------------
    @abstractmethod
    def calcular_bonus(self) -> float:
        pass

    @abstractmethod
    def calcular_descontos(self) -> float:
        pass

    @abstractmethod
    def calcular_adicionais(self) -> float:
        pass