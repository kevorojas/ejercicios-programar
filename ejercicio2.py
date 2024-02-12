import math

def calcularAreaYPerimetroCircunferencia(radio):
    """
    Calcula el área y el perímetro de una circunferencia dado su radio.

    Args:
        radio (float): El radio de la circunferencia.

    Returns:
        tuple: Una tupla con el área y el perímetro de la circunferencia, respectivamente.
    """
    area = math.pi * radio ** 2  # Calcula el área usando la fórmula A = π * r^2
    perimetro = 2 * math.pi * radio  # Calcula el perímetro usando la fórmula P = 2 * π * r
    return area, perimetro  # Retorna una tupla con el área y el perímetro

def main():
    """
    Función principal que solicita al usuario el radio de una circunferencia,
    calcula su área y perímetro, e imprime los resultados.
    """
    try:
        radio = float(input("Ingrese el radio de la circunferencia: "))  # Solicita al usuario que ingrese el radio
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo.")  # Lanza una excepción si el radio es negativo o cero

        area, perimetro = calcularAreaYPerimetroCircunferencia(radio)  # Calcula el área y el perímetro

        print("El área de la circunferencia es:", area)  # Imprime el área
        print("El perímetro de la circunferencia es:", perimetro)  # Imprime el perímetro
    except ValueError as e:
        print("Error:", e)  # Imprime un mensaje de error si ocurre una excepción

if __name__ == "__main__":
    main()  # Llama a la función principal si se ejecuta este script como el programa principal
