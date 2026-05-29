
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

# 📋 Requisitos funcionais

---

## 🥕 RF01 – Cadastro de Ingredientes
👨‍🍳 Como gerente do restaurante,  
📦 eu quero cadastrar ingredientes com nome, quantidade e data de validade,  
🎯 para controlar o estoque de produtos perecíveis.

---

## 📊 RF02 – Atualização de Estoque
👨‍🔧 Como operador de estoque,  
📦 eu quero atualizar a quantidade dos ingredientes,  
🎯 para manter o controle correto dos itens disponíveis.

---

## 📦 RF03 – Consulta de Estoque
👩‍🍳 Como funcionário do restaurante,  
📋 eu quero visualizar o estoque de ingredientes,  
🎯 para saber o que está disponível para uso.

---

## 🍛 RF04 – Cadastro de Pratos
👨‍🍳 Como gerente do restaurante,  
📦 eu quero cadastrar pratos com seus ingredientes e quantidades,  
🎯 para automatizar o consumo de estoque nas vendas.

---

## 💰 RF05 – Venda de Pratos
💳 Como operador de caixa,  
🧾 eu quero registrar a venda de pratos no sistema,  
🎯 para que o estoque seja atualizado automaticamente.

---

## 🔄 RF06 – Baixa Automática de Estoque
⚙️ Como sistema do restaurante,  
📉 eu quero reduzir automaticamente os ingredientes após a venda de um prato,  
🎯 para manter o estoque sempre atualizado.

---

## 🍽️ RF07 – Controle do Prato Feito
👨‍🍳 Como gerente do restaurante,  
🍛 eu quero que o sistema saiba a composição do “Prato Feito”,  
🎯 para garantir a baixa correta de 200g de arroz e 100g de feijão.

---

## ⚠️ RF08 – Alerta de Validade Próxima
🚨 Como gerente do restaurante,  
📅 eu quero receber alertas de ingredientes com validade menor que 3 dias,  
🎯 para evitar desperdício de alimentos.

---

## ❌ RF09 – Bloqueio de Venda por Falta de Estoque
🚫 Como operador de caixa,  
🧾 eu quero que o sistema bloqueie a venda de pratos sem ingredientes suficientes,  
🎯 para evitar erros na venda.

---

## 🗂️ RF10 – Controle de Validade dos Ingredientes
📅 Como gerente do restaurante,  
📦 eu quero visualizar a data de validade de cada ingrediente,  
🎯 para organizar o uso dos produtos antes que estraguem.

---

## 📈 RF11 – Relatório de Estoque
📊 Como gerente do restaurante,  
📑 eu quero gerar relatórios do estoque atual,  
🎯 para analisar consumo e reposição de ingredientes.

---

## 🔔 RF12 – Notificação de Baixo Estoque
🚨 Como gerente do restaurante,  
📦 eu quero ser avisado quando um ingrediente estiver acabando,  
🎯 para evitar falta de produtos no restaurante.

---

# 📜 Regras de Negócio (RN)

---

## ⚠️ RN01 – Controle de Validade
Ingredientes com menos de 3 dias para o vencimento devem aparecer em destaque no sistema.

---

## 🍛 RN02 – Consumo do Prato Feito
Ao vender um “Prato Feito”, o sistema deve retirar automaticamente:  
- 🍚 200g de arroz  
- 🫘 100g de feijão  

---

## ❌ RN03 – Validação de Estoque Obrigatória
O sistema só pode concluir uma venda se todos os ingredientes do prato estiverem disponíveis em quantidade suficiente.

---

# ⚙️ Requisitos Não Funcionais (RNF)

---

## 🚀 RNF01 – Desempenho
Como usuário do sistema,  
⏱️ eu quero que a atualização do estoque aconteça em até 5 minutos após uma venda,  
🎯 para garantir que os dados estejam sempre atualizados.

---

## 🔐 RNF02 – Segurança
Como usuário do sistema,  
🔒 eu quero que minhas credenciais sejam armazenadas de forma criptografada,  
🎯 para garantir a segurança das informações e acesso protegido ao sistema.

---

✨ **StockFlow – Controle inteligente para um restaurante sem desperdícios!**

---
