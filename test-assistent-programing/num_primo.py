def eh_primo(n: int) -> bool:
    """
    Verifica se um número é primo.

    Um número primo é um inteiro maior que 1 que possui apenas dois divisores positivos: 1 e ele mesmo.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se n for primo, False caso contrário.

    Raises:
        Nenhum, mas retorna False para entradas não inteiras ou inválidas.
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

    # Elimina múltiplos de 2 e 3
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
    # Executa testes automáticos se houver argumentos de linha de comando
    import sys
    if len(sys.argv) > 1:
        print("Testando a função eh_primo com lista pré-definida:")
        for numero in TEST_NUMBERS:
            resultado = eh_primo(numero)
            status = "primo" if resultado else "não primo"
            print(f"{numero}: {status}")
    else:
        # Modo interativo: solicita entrada do usuário
        try:
            numero = int(input("Digite um número inteiro para verificar se é primo: "))
            resultado = eh_primo(numero)
            status = "primo" if resultado else "não primo"
            print(f"O número {numero} é {status}.")
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")
