# Gerenciamento de Transporte Público

Sistema simples de cartão de transporte público desenvolvido em **Python** para a disciplina **MI - Algoritmos e Programação 1** (Metodologia de Implementação) na UEFS para o curso de Engenharia da Computação, utilizando **Problem Based Learning (PBL)**.

Simula o gerenciamento de saldo em TechVille: recargas, compra de passagens com descontos por categoria, verificação de embarque e relatórios.

**Restrições impostas pela disciplina:** sem uso de funções (`def`), `try/except` ou `break`. Tudo resolvido com `while`, condicionais e validações manuais.

<p align="center">
  <img src="imagens/exemplo-menu.png" alt="Menu do Sistema" width="500"/>
</p>

## 👤 Autor

- **Gustavo Silva Ribeiro**
- **Bacharelando em Engenharia da Computação – UEFS**
- **Email: gustavosr.comp@gmail.com**

## ✨ Funcionalidades

- Configuração do valor da passagem
- Recarga de saldo por categoria: Padrão, Estudante/Idoso (50% desconto), Social (80% desconto)
- Compra de passagem com desconto automático
- Verificação de embarque (debita passagem comprada)
- Consulta de saldo atual
- Geração de relatório com totais: recargas, quantidades, gastos, saldos restantes e passagens usadas
- Validação rigorosa de entradas (apenas números positivos, sem ponto múltiplo)

## 🛠️ Tecnologias

- **Linguagem:** Python 3.13.2
- **Ambiente:** Visual Studio Code + Windows 11
- **Estruturas usadas:** Variáveis, `while`, `if/elif/else`, `match/case`, métodos de string como `.strip()`, `.replace()`, `.isdigit()`

## 📄 Documentação e Código

- **Código fonte:** [src/Gerenciamento_Transporte_Publico-estrutura_v2.6.py]
- **Relatório técnico:** [Relatório (PDF) - Docs/Relatório do problema 1 - Gustavo Silva Ribeiro-1.pdf]

## 🚀 Como Executar

1. Clone o repositório:
   ```bash python src/Gerenciamento_Transporte_Publico-estrutura_v2.6 - PBL 1
   git clone https://github.com/gustavo-ec/Gerenciamento-de-Transporte-Publico.git
   cd Gerenciamento-de-Transporte-Publico
   python src/Gerenciamento_Transporte_Publico-estrutura_v2.6.py
