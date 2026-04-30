
---

# Projeto: Refatoração e Debug em Python

Este repositório contém uma coleção de scripts Python que passaram por um processo de **debugging** e **refatoração**. O objetivo principal foi transformar códigos funcionais, porém mal estruturados, em scripts robustos, legíveis e eficientes, seguindo as melhores práticas de *Clean Code*.

## Conteúdo do Repositório

O projeto está dividido em três frentes principais:

1.  **Recibo de Vendas (`debug.py`)**: Correção de erros de sintaxe e lógica em um sistema de PDV simples.
2.  **Verificador de Números Primos (`num_primo.py`)**: Implementação de um algoritmo matemático otimizado ($6k \pm 1$).
3.  **Estatísticas de Dados (`refatoracao.py`)**: Transformação de código legado em funções idiomáticas de Python.

---

## Detalhes dos Arquivos

### 1. Sistema de Vendas (`debug.py`)
Este script gerencia a entrada de produtos, calcula subtotal, aplica impostos e descontos percentuais.

*   **Bugs Corrigidos:**
    *   Falta de aspas em strings de `input`.
    *   Erro de tipo (*TypeError*) ao tentar realizar cálculos matemáticos com strings.
    *   Erros de indentação no bloco `if`.
    *   Ausência de *f-strings* em saídas formatadas.
*   **Melhorias:** Adição de `round()` para precisão financeira e validação visual de desconto.

### 2. Verificador de Números Primos (`num_primo.py`)
Um script de alta performance para verificar a primalidade de um número.

*   **Destaque Técnico:** Utiliza a lógica de que todos os primos maiores que 3 seguem a forma $6k \pm 1$.

*   **Funcionalidades:**
    *   **Type Hints:** Maior clareza sobre os tipos de dados esperados.
    *   **Modo Híbrido:** Pode ser executado de forma interativa ou via terminal passando argumentos (ex: `python num_primo.py test`) para rodar uma bateria de testes automáticos.
    *   **Tratamento de Erros:** Bloco `try-except` para evitar falhas com entradas não numéricas.

### 3. Estatísticas de Dados (`refatoracao.py`)
Exemplo prático de refatoração de código "espaguete" para Python Moderno.

*   **Antes:** Variáveis como `a, b, c, d` e loops manuais para soma e busca de valores.
*   **Depois:** Uso de funções nativas (`sum`, `max`, `min`) e nomes de variáveis semânticos.
*   **Complexidade:** Redução de linhas de código e aumento drástico da manutenibilidade.

---

## Como Executar

Certifique-se de ter o **Python 3.10+** instalado em sua máquina.

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Execute o verificador de primos (modo interativo):
   ```bash
   python num_primo.py
   ```

3. Execute o script de estatísticas:
   ```bash
   python refatoracao.py
   ```

---

## Princípios de Clean Code Aplicados

*   **Nomenclatura Significativa:** Variáveis e funções agora revelam sua intenção (ex: de `c(l)` para `calculate_statistics(numbers)`).
*   **DRY (Don't Repeat Yourself):** Eliminação de loops redundantes em favor de funções *built-in*.
*   **Documentação (Docstrings):** Todas as funções principais incluem explicação de parâmetros, retornos e exemplos de uso.
*   **Single Responsibility Principle:** Cada função ou script foca em resolver apenas um problema específico.

---
*Desenvolvido com foco em qualidade de código e lógica computacional.*
```