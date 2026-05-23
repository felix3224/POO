from folha_pagamento.funcionario import Funcionario

# Desenvolva a classe Estagiario aqui.


class Estagiario(Funcionario):
    def __init__(self, nome, matricula, salario_base, curso, carga_horaria):
        super().__init__(nome, matricula, salario_base)
        self.curso = curso
        self.carga_horaria = carga_horaria

    def calcular_bonus(self):
        return self._salario_base * (3 / 100)

    def calcular_descontos(self):
        return self._salario_base * 0.02

    def calcular_adicionais(self):
        if self.carga_horaria <= 20:
            return 150

        elif self.carga_horaria <= 30:
            return 250

        else:
            return 350
