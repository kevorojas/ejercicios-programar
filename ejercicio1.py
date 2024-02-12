def calcularMaxMin(lista):
    """
    Función que recibe una lista de valores numéricos y devuelve el valor máximo y mínimo.

    Args:
        lista (list): Lista de valores numéricos.

    Returns:
        tuple: Una tupla con el valor máximo y mínimo de la lista, respectivamente.
    """
    if not lista:  # Verifica si la lista está vacía
        return None, None  # Retorna None para ambos valores máximo y mínimo
    maximo = minimo = lista[0]  # Inicializa los valores máximo y mínimo con el primer elemento de la lista
    for num in lista:  # Itera sobre cada elemento en la lista
        if num > maximo:  # Si el número actual es mayor que el máximo encontrado hasta ahora
            maximo = num  # Actualiza el valor máximo
        if num < minimo:  # Si el número actual es menor que el mínimo encontrado hasta ahora
            minimo = num  # Actualiza el valor mínimo
    return maximo, minimo  # Retorna una tupla con el valor máximo y mínimo


def main():
    """
    Función principal que solicita números al usuario, calcula el máximo y mínimo, e imprime el resultado.
    """
    numeros = []  # Lista para almacenar los números ingresados por el usuario
    while True:  # Bucle infinito para solicitar números hasta que se ingrese "fin"
        entrada = input("Ingrese un número (o 'fin' para terminar): ")  # Solicita un número al usuario
        if entrada.lower() == 'fin':  # Verifica si se ingresó "fin" para terminar el bucle
            break  # Sale del bucle
        try:
            numero = float(entrada)  # Intenta convertir la entrada a un número flotante
            numeros.append(numero)  # Agrega el número a la lista de números
        except ValueError:
            print("Por favor, ingrese un número válido.")  # Imprime un mensaje de error si la entrada no es válida

    maximo, minimo = calcularMaxMin(numeros)  # Calcula el máximo y mínimo de la lista de números
    if maximo is not None and minimo is not None:  # Verifica si se encontraron valores máximo y mínimo
        print("El máximo es:", maximo)  # Imprime el valor máximo
        print("El mínimo es:", minimo)  # Imprime el valor mínimo
    else:
        print("No se ingresaron números.")  # Imprime un mensaje si no se ingresaron números


if __name__ == "__main__":
    main()  # Llama a la función principal si se ejecuta este script como el programa principal
