
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

## 🥗 Requisitos Funcionais (RF)

| ID | Requisito | Descrição |
|----|----------|-----------|
| RF01 | Cadastro de Ingredientes | Permitir cadastrar ingredientes com nome, quantidade e validade |
| RF02 | Atualização de Estoque | Atualizar automaticamente a quantidade dos ingredientes |
| RF03 | Consulta de Estoque | Visualizar ingredientes disponíveis |
| RF04 | Cadastro de Pratos | Cadastrar pratos com seus ingredientes |
| RF05 | Registro de Vendas | Registrar vendas no sistema |
| RF06 | Baixa Automática | Reduzir estoque automaticamente após venda |
| RF07 | Controle do Prato Feito | Aplicar consumo fixo (200g arroz, 100g feijão) |
| RF08 | Alerta de Validade | Avisar quando faltar menos de 3 dias para vencer |
| RF09 | Bloqueio de Venda | Impedir venda sem estoque suficiente |
| RF10 | Controle de Validade | Mostrar data de validade dos ingredientes |
| RF11 | Relatórios de Estoque | Gerar relatórios de consumo e estoque |
| RF12 | Notificação de Baixo Estoque | Avisar quando ingredientes estiverem acabando |

---

## ⚙️ Requisitos Não Funcionais (RNF)

| ID | Requisito | Descrição |
|----|----------|-----------|
| RNF01 | Desempenho | Atualizar estoque em até 5 minutos após venda |
| RNF02 | Segurança | Armazenar senhas de forma criptografada |

---

## 📜 Regras de Negócio (RN)

| ID | Regra | Descrição |
|----|------|-----------|
| RN01 | Controle de Validade | Ingredientes com menos de 3 dias devem ser destacados |
| RN02 | Consumo do Prato Feito | Consumir automaticamente arroz e feijão na venda |
| RN03 | Validação de Estoque | Impedir venda sem ingredientes suficientes |

---

✨ **StockFlow – Inteligência no controle de estoque, menos desperdício e mais eficiência!** 🍽️📦
