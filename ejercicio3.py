def calcularTemperaturaMedia(temperatura_max, temperatura_min):
    """
    Calcula la temperatura media de un día a partir de la temperatura máxima y mínima.

    Args:
        temperatura_max (float): La temperatura máxima del día.
        temperatura_min (float): La temperatura mínima del día.

    Returns:
        float: La temperatura media del día.
    """
    temperatura_media = (temperatura_max + temperatura_min) / 2
    return temperatura_media

def main():
    """
    Función principal que solicita al usuario el número de días y las temperaturas máxima y mínima de cada día,
    calcula la temperatura media de cada día, e imprime los resultados.
    """
    try:
        num_dias = int(input("Ingrese el número de días: "))  # Solicita al usuario el número de días
        if num_dias <= 0:
            raise ValueError("El número de días debe ser un entero positivo.")  # Lanza una excepción si el número de días es negativo o cero

        for dia in range(1, num_dias + 1):  # Itera sobre cada día
            temperatura_max = float(input(f"Ingrese la temperatura máxima del día {dia}: "))  # Solicita la temperatura máxima del día
            temperatura_min = float(input(f"Ingrese la temperatura mínima del día {dia}: "))  # Solicita la temperatura mínima del día

            temperatura_media = calcularTemperaturaMedia(temperatura_max, temperatura_min)  # Calcula la temperatura media

            print(f"La temperatura media del día {dia} es: {temperatura_media:.2f} grados Celsius")  # Imprime la temperatura media
    except ValueError as e:
        print("Error:", e)  # Imprime un mensaje de error si ocurre una excepción

if __name__ == "__main__":
    main()  # Llama a la función principal si se ejecuta este script como el programa principal
