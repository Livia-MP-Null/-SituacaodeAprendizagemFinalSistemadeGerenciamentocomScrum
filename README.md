
# 🍽️ StockFlow – Sistema de Estoque para Restaurante


<img width="1683" height="934" alt="image" src="https://github.com/user-attachments/assets/4ff17b76-156f-45b3-b55f-ea636766f466" />


✨ Controle inteligente de ingredientes, validade e vendas ✨

---
# 👥 Integrantes

| Nome | Curso |
|------|--------|
| **Livia de Melo Pondian** | Desenvolvimento de Sistemas |
| **Henrique Martines Teixeira** | Desenvolvimento de Sistemas |


## 📌 1. Briefing do Sistema

O cliente é um restaurante que trabalha com produtos perecíveis e precisa de um sistema para controlar melhor o estoque de ingredientes. Atualmente, o controle manual gera problemas como desperdício de alimentos, erros na quantidade disponível e dificuldade em acompanhar a validade dos produtos.

O sistema deve permitir o cadastro de ingredientes com suas quantidades e datas de validade, além de controlar automaticamente o estoque após cada venda. Também é necessário que o sistema emita alertas quando algum ingrediente estiver próximo de vencer (menos de 3 dias).

Outra necessidade importante é o controle dos pratos vendidos, especialmente o **“Prato Feito”**, que deve reduzir automaticamente 200g de arroz e 100g de feijão do estoque. Além disso, o sistema não pode permitir a venda de pratos caso faltem ingredientes suficientes.

🎯 **Objetivo:** automatizar o controle de estoque, reduzir desperdícios, evitar erros e melhorar a gestão do restaurante.

---

# 🍽️ StockFlow – Sistema de Estoque para Restaurante

---

## 📘 1. Introdução (IEEE 29148:2018)

Este documento de requisitos foi elaborado com base no padrão **IEEE 29148:2018**, que define boas práticas para especificação de requisitos de software.

O objetivo do sistema **StockFlow** é fornecer um controle eficiente de estoque para um restaurante que trabalha com produtos perecíveis, reduzindo desperdícios, automatizando processos e garantindo maior precisão no controle de ingredientes e vendas.

---

## 📖 2. Descrição Geral do Sistema

O sistema StockFlow será responsável por gerenciar o estoque de um restaurante, permitindo:

- 📦 Cadastro de ingredientes com validade e quantidade  
- 🍛 Cadastro de pratos e suas composições  
- 💰 Registro de vendas com baixa automática de estoque  
- ⚠️ Alertas de validade próxima (menos de 3 dias)  
- ❌ Bloqueio de vendas quando não houver ingredientes suficientes  

O sistema também garante controle automático de consumo, especialmente no caso do “Prato Feito”, que possui regras fixas de consumo de ingredientes.

---

# 📊 3. Tabelas de Requisitos

---

# Requisitos Funcionais (RF)

| Código | Requisito |
|---------|-----------|
| RF01 | Criação de Usuários |
| RF02 | Cadastro de Ingredientes |
| RF03 | Consulta de Estoque |
| RF04 | Cadastro de Pratos |
| RF05 | Venda de Pratos |
| RF06 | Histórico |
| RF07 | Baixa Automática de Estoque |
| RF08 | Baixa de Estoque Composta |

---

# Regras de Negócio (RN)

| Código | Regra de Negócio |
|---------|------------------|
| RN01 | Alerta de Validade |
| RN02 | Validade Próxima |
| RN03 | Consumo dos Pratos |
| RN04 | Bloqueio de Venda |
| RN05 | Não permitir venda sem ingredientes |

---

# Requisitos Não Funcionais (RNF)

| Código | Requisito Não Funcional |
|---------|------------------------|
| RNF01 | Facilidade de Uso |
| RNF02 | Senha para usuário da empresa |
| RNF03 | Desempenho |
|
| RN02 | Consumo do Prato Feito | Consumir automaticamente arroz e feijão na venda |
| RN03 | Validação de Estoque | Impedir venda sem ingredientes suficientes |

---
---

# 📋 Kanban do Projeto

As imagens abaixo representam a evolução do quadro Kanban do projeto **StockFlow**, demonstrando a organização das tarefas ao longo do desenvolvimento.

## 📝 Visão Geral

O Kanban foi utilizado para acompanhar o andamento das atividades, separando as tarefas em etapas como:

- 📌 A Fazer (To Do)
- 🚧 Em Desenvolvimento (Doing)
- ✅ Concluído (Done)

Essa metodologia permitiu melhor controle das entregas, organização da equipe e acompanhamento do progresso do projeto.

---

## 📸 Registro da Evolução do Kanban

### 📍 Imagem 1
**Descrição:** Estado inicial do quadro Kanban com as primeiras tarefas planejadas para o desenvolvimento do sistema.

<img width="1426" height="509" alt="image" src="https://github.com/user-attachments/assets/ea8b1c1d-6b88-4b7c-80c4-5e8fbb458272" />


---

### 📍 Imagem 2
**Descrição:** Organização das tarefas e definição das atividades prioritárias do projeto.

<img width="1406" height="459" alt="image" src="https://github.com/user-attachments/assets/3cfea478-ff8d-43c8-b2aa-81268b675bf5" />


---

### 📍 Imagem 3
**Descrição:** Início da movimentação das tarefas para a etapa de desenvolvimento.

<img width="1416" height="449" alt="image" src="https://github.com/user-attachments/assets/6ebb8221-f493-48d0-affb-859f740f4664" />



---

### 📍 Imagem 4
**Descrição:** Avanço das funcionalidades principais do sistema e acompanhamento do progresso.

<img width="1425" height="469" alt="image" src="https://github.com/user-attachments/assets/3a5d96c0-97c9-4e4f-aa5f-70c99f236c96" />


---

### 📍 Imagem 5
**Descrição:** Continuidade do desenvolvimento e atualização das tarefas concluídas.

<img width="1426" height="422" alt="image" src="https://github.com/user-attachments/assets/090d57fb-4e83-4427-af61-036ff27cdebb" />



---

### 📍 Imagem 6
**Descrição:** Evolução das implementações e validação das funcionalidades desenvolvidas.


<img width="1412" height="450" alt="image" src="https://github.com/user-attachments/assets/046bb16f-730a-4de3-baef-4fcecd264188" />

---

### 📍 Imagem 7
**Descrição:** Organização das atividades restantes para finalização do projeto.
<img width="1576" height="438" alt="image" src="https://github.com/user-attachments/assets/b9b02261-96c4-4f0c-8bc8-3db5b8211666" />



---

### 📍 Imagem 8
**Descrição:** Consolidação das entregas e revisão das tarefas executadas.

<img width="1656" height="376" alt="image" src="https://github.com/user-attachments/assets/9b9688e8-ccf9-405b-991a-d822355c5db6" />


---

### 📍Kanban da programação
**Descrição:** Registro intermediário do progresso geral do projeto.

<img width="1285" height="706" alt="image" src="https://github.com/user-attachments/assets/3d228145-e089-41aa-b45a-54e1677d19c5" />


---

### 📍 Imagem 10
**Descrição:** Atualização do quadro com foco na conclusão das atividades pendentes.

<img width="1787" height="619" alt="image" src="https://github.com/user-attachments/assets/c9f6d601-bafc-4ca8-8848-9e8f5ed9789b" />

---

### 📍 Imagem 11
**Descrição:** Revisão das tarefas e preparação para os testes finais.

<img width="1699" height="555" alt="image" src="https://github.com/user-attachments/assets/b0525278-0462-41fc-addf-520b633c82a5" />



---

### 📍 Imagem 12
**Descrição:** Acompanhamento do encerramento das etapas de desenvolvimento.

<img width="1529" height="573" alt="image" src="https://github.com/user-attachments/assets/bef7e42b-564f-4b30-bc19-8b36f8d02812" />


---

### 📍 Imagem 13
**Descrição:** Verificação do cumprimento dos requisitos do sistema.

<img width="1546" height="614" alt="image" src="https://github.com/user-attachments/assets/191a97e5-9bce-4f21-83a6-fcfd435a944e" />


---

### 📍 Imagem 14
**Descrição:** Ajustes finais e organização das últimas atividades.

<img width="1554" height="641" alt="image" src="https://github.com/user-attachments/assets/4bf6990d-69fa-421a-8399-133587cc97a6" />


---

### 📍 Imagem 15
**Descrição:** Conclusão das funcionalidades previstas no escopo.

<img width="1667" height="724" alt="image" src="https://github.com/user-attachments/assets/b52ee2c0-7e29-4e41-9c9e-b9f72fe98394" />

---

## 🎯 Considerações Finais

A utilização do método Kanban contribuiu para a organização do projeto **StockFlow**, permitindo acompanhar o progresso das tarefas, identificar prioridades e garantir que os requisitos fossem desenvolvidos dentro do cronograma planejado.Por isso utilizamos-o

## Validações

Identificamos áreas que necessitavam de validação e conseguimos corrigir algumas delas. No entanto, ainda existem casos pendentes, como o processo de compra de alimentos, que requer novos ajustes.

✨ **StockFlow – Inteligência no controle de estoque, menos desperdício e mais eficiência!** 🍽️📦
