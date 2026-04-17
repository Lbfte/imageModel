def calculate_statistics(numbers: list[int]) -> tuple[int, float, int, int]:
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numbers: Lista de números para análise.
    
    Returns:
        Tupla contendo (total, média, máximo, mínimo).
    """
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum


# Dados de exemplo
data = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

# Calcular e exibir estatísticas
total, average, maximum, minimum = calculate_statistics(data)

print("Total:", total)
print("Média:", average)
print("Maior:", maximum)
print("Menor:", minimum)