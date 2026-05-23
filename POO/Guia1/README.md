# Guia 1 - Carregando Dados


Este projeto tem como objetivo praticar conceitos de Programação Orientada a Objetos (POO) em Python, utilizando uma aplicação simples baseada em leitura de arquivos, criação de objetos e processamento em memória.

---

## 🎯 Objetivo

Você deve analisar o código existente e implementar melhorias para que o sistema:

- Valide corretamente os dados carregados do arquivo
- Permita buscas mais avançadas
- Passe em todos os testes automatizados

---

## ▶️ Como executar

### Executar aplicação


python -m src.main


### Executar testes


python -m tests.test_runner


---

## ✅ Critério de sucesso

Ao executar os testes, o resultado esperado é:

- Todos os testes com status **OK**
- Nenhuma mensagem contendo **FALHA**

Se houver qualquer **FALHA**, o sistema ainda está incorreto.

---

## 🧩 ISSUE 1 — Validação de Dados

### Problema

O sistema atualmente carrega dados do arquivo sem validação.

Isso permite registros inválidos, como:
- ID vazio ou negativo
- Nome vazio
- Endereço vazio

---

### Sua tarefa

Implementar validação para garantir que:

- `id` seja inteiro positivo
- `name` não seja vazio
- `address` não seja vazio

---

### Regras

- Registros inválidos devem ser ignorados
- O sistema deve continuar funcionando normalmente
- Deve ser exibida mensagem indicando o erro

---

### Exemplo esperado


Registro inválido ignorado: {'id': '', 'name': 'Sem ID', 'address': 'Rua C'}


---

### Onde implementar

- `models/record.py`
ou
- `repositories/record_repository.py`

---

## 🧩 ISSUE 2 — Busca com Múltiplos Termos

### Problema

A busca atual aceita apenas um termo simples.

---

### Sua tarefa

Permitir que o usuário informe múltiplos termos:


joao rua a


---

### Regras

- Separar a entrada em palavras
- A busca deve ser:
  - Case-insensitive
  - Aplicada em `name` e `address`
- O registro só deve ser retornado se contiver **todos os termos**

---

### Exemplo esperado

Entrada:

joao rua a


Saída:

Record(id=1, name='João Silva', address='Rua A 123')


---

### Onde implementar

- `services/record_service.py`
ou
- `repositories/record_repository.py`

---

## 🧪 Sobre os testes

O arquivo:


tests/test_runner.py


executa automaticamente:

- Carregamento de dados
- Validação de registros inválidos
- Busca com múltiplos termos

---

## ⚠️ Importante

- Não altere os testes
- Corrija apenas o código da aplicação
- O objetivo é fazer o sistema passar nos testes corretamente

---

## 💡 Dica

Se você precisar escolher onde implementar a lógica:

- **Validação → Model ou Repository**
- **Regra de busca → Service ou Repository**

Essa decisão faz parte da avaliação.

---

## 🚀 Resultado esperado

Ao final, o sistema deve:

- Carregar apenas dados válidos
- Permitir buscas avançadas
- Executar todos os testes sem falhas


OK: Registros carregados
OK: Registros inválidos ignorados corretamente
OK: Busca múltiplos termos funcionando


---

## 📌 Conclusão

Se passou nos testes sem falhas:

✔ Você implementou corretamente  
✔ Você entendeu a separação de responsabilidades  
✔ Você aplicou POO de forma prática  

Caso contrário: revise sua modelagem.
>>77f39f6cb45e487337a25f811b074ceb<<