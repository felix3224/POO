# Guia 2 — Sistema de Folha de Pagamento (RH)

## Contexto

Você faz parte da equipe responsável por manter um módulo de **Folha de Pagamento** dentro de um sistema de **Recursos Humanos (RH)**.

Esse módulo calcula informações básicas de funcionários de diferentes cargos, como:

- nome
- matricula
- salario_base

Atualmente o sistema possui uma hierarquia de classes para representar funcionários, mas carece implementar as subclasses de acordo com o diagrama UML abaixo:

                     --------------------------------
                     |   Funcionario                |
                     --------------------------------
                     | - nome                       |
                     | - matricula                  |
                     | - salario_base               |
                     --------------------------------
                     | + dados_basicos()            |
                     | + gerar_contracheque()       |
                     | + calcular_salario_liquido() |
                     | # calcular_bonus()           |
                     | # calcular_descontos()       |
                     | # calcular_adicionais()      |
                     --------------------------------
                                    ▲
                -----------------------------------------
                |                   |                   |
                |                   |                   |
        -----------------   -----------------   -----------------
        | Desenvolvedor |   |    Gerente    |   |  Estagiari o  |
        -----------------   -----------------   -----------------
        | linguagem     |   | setor         |   | curso         |
        | senioridade   |   | qtd_equipe    |   | carga_horaria |
        -----------------   -----------------   -----------------

Seu papel é implementar as subclasses passando nos testes propostos.

---

## 1. Desenvolvedor

### Atributos adicionais

- `linguagem`
- `senioridade`

### Regras

#### `calcular_bonus()`

O bônus depende da senioridade:

| Senioridade | Bônus                |
|-------------|----------------------|
| junior      | 5% do salário base   |
| pleno       | 10% do salário base  |
| senior      | 15% do salário base  |

---

#### `calcular_descontos()`

Desconto fixo de **8% do salário base**.

---

#### `calcular_adicionais()`

Adicional definido pela linguagem principal:

| Linguagem      | Adicional |
|----------------|-----------|
| Python         | +500      |
| Java           | +400      |
| JavaScript     | +350      |
| Qualquer outra | +200      |

---

## 2. Gerente

### Atributos adicionais

- `setor`
- `qtd_equipe`

### Regras

#### `calcular_bonus()`

O bônus depende da quantidade de pessoas na equipe:

| Tamanho da equipe | Bônus               |
|-------------------|---------------------|
| até 5             | 10% do salário base |
| de 6 até 10       | 15% do salário base |
| acima de 10       | 20% do salário base |

---

#### `calcular_descontos()`

Desconto fixo de **12% do salário base**.

---

#### `calcular_adicionais()`

Adicional por responsabilidade:

| Quantidade da equipe | Adicional |
|----------------------|-----------|
| equipe > 10          | +2000     |
| equipe > 5           | +1000     |
| caso contrário       | +500      |

---

## 3. Estagiario

### Atributos adicionais

- `curso`
- `carga_horaria`

### Regras

#### `calcular_bonus()`

Bônus fixo de **3% do salário base**.

---

#### `calcular_descontos()`

Desconto fixo de **2% do salário base**.

---

#### `calcular_adicionais()`

Auxílio baseado na carga horária:

| Carga horária | Adicional |
|---------------|-----------|
| até 20h       | +150      |
| até 30h       | +250      |
| acima de 30h  | +350      |

---
995b5983a8b684cba7bbc7f802c760906f0d690c1e90bf440631cfe486082eb3