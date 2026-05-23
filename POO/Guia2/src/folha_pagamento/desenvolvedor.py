from folha_pagamento.funcionario import Funcionario

# Desenvolva a classe Desenvolvedor aqui.


class Desenvolvedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, linguagem, senioridade):
        super().__init__(nome, matricula, salario_base)
        self.linguagem = linguagem
        self.senioridade = senioridade

    def calcular_bonus(self):
        if self.senioridade == "junior":
            bonus = 5 / 100
            return self._salario_base * bonus

        if self.senioridade == "pleno":
            bonus = 10 / 100
            return self._salario_base * bonus

        if self.senioridade == "senior":
            bonus = 15 / 100
            return self._salario_base * bonus

    def calcular_descontos(self):
        return self._salario_base * (8 / 100)

    def calcular_adicionais(self):

        if self.linguagem == "Python":
            return 500
        if self.linguagem == "Java":
            return 400
        if self.linguagem == "JavaScript":
            return 350
        else:
            return 200
