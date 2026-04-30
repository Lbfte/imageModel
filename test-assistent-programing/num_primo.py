import sys

def eh_primo(n: int) -> bool:
    """Verifica se um número inteiro é primo.

    Um número primo é definido como um número inteiro maior que 1 que possui 
    exatamente dois divisores positivos distintos: 1 e ele mesmo. Esta função 
    utiliza uma otimização baseada no teste de divisibilidade 6k ± 1 para 
    aumentar a eficiência em números grandes.

    Args:
        n (int): O número inteiro a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário (incluindo 
            números menores que 2 ou entradas de tipos diferentes de int).

    Examples:
        >>> eh_primo(7)
        True
        >>> eh_primo(10)
        False
    """
    # Verifica se a entrada é um inteiro
    if not isinstance(n, int):
        return False

    # Números menores ou iguais a 1 não são primos
    if n <= 1:
        return False

    # 2 e 3 são primos
    if n <= 3:
        return True

    # Elimina múltiplos de 2 e 3 rapidamente
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Verifica divisibilidade por números da forma 6k ± 1 até a raiz quadrada de n
    # Isso otimiza o algoritmo, reduzindo verificações desnecessárias
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


# Constantes para testes (lista de números para validar a função)
TEST_NUMBERS = [
    -5,  # Negativo
    0,   # Zero
    1,   # Um
    2,   # Primo par
    3,   # Primo ímpar pequeno
    4,   # Composto
    17,  # Primo maior
    19,  # Primo maior
    20,  # Composto
    23,  # Primo
    24,  # Composto
    97,  # Primo grande
    100, # Composto
]

if __name__ == "__main__":
    # Se houver argumentos na linha de comando, executa a bateria de testes
    if len(sys.argv) > 1:
        print("Executando testes automáticos:")
        print("-" * 30)
        for numero in TEST_NUMBERS:
            resultado = eh_primo(numero)
            status = "PRIMO" if resultado else "não primo"
            print(f"{numero:>4}: {status}")
    else:
        # Modo interativo padrão
        try:
            entrada = input("Digite um número inteiro para verificar se é primo: ")
            numero_usuario = int(entrada)
            
            if eh_primo(numero_usuario):
                print(f"✨ O número {numero_usuario} é PRIMO.")
            else:
                print(f"❌ O número {numero_usuario} NÃO é primo.")
                
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros válidos.")