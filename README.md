
# 🍽️ StockFlow – Sistema de Estoque para Restaurante


<img width="1683" height="934" alt="image" src="https://github.com/user-attachments/assets/4ff17b76-156f-45b3-b55f-ea636766f466" />


✨ Controle inteligente de ingredientes, validade e vendas ✨

---

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

✨ **StockFlow – Inteligência no controle de estoque, menos desperdício e mais eficiência!** 🍽️📦
