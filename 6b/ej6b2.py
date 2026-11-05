"""
Enunciado:
Utilizando un depurador de código para Python. Corrije el error de la
función llamada 'average_of_even_numbers(numbers)' que acepta una lista de
números enteros como entrada y calcula el promedio de todos los números pares
en la lista.

Para depurar el código se puede usar pdb o herramientas de depuración
externas.

La función debe devolver un número flotante redondeado a dos decimales. Si no
hay números pares en la lista, la función debe devolver 0.

Parámetros:
    numbers: una lista de números enteros.

Ejemplo:
    Entrada:
        numbers = [2, 3, 4, 5, 6]
    Salida:
        4.0
"""


from typing import List

    
def average_of_even_numbers(numbers):
    total = 0
    counter = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
            counter += 1
    if counter == 0:
        return 0.0
    else:
        return round(total / counter, 2)


numbers = [2, 3, 4, 5, 6]
result = average_of_even_numbers(numbers)
print(result)
