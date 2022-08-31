countries = ['USA', 'UK', 'Canada']
populations = [329.5, 67.5, 38, 58, 98]

for country, population in zip(countries, populations):
    print(country)
    print(population)
    print(f'{country} tiene una poblacion de {population}')


def custom_max(n1, n2):
    """
    Dado dos numeros de entrada devolver el número mayor
    Args:
        n1: primer numero a comparar
        n2: segundo numero a comparar

    Returns:
        int : mayor de ambos
    """
    return n
