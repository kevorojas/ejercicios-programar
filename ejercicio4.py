def ConvertirEspaciado(texto):
    """
    Recibe un texto y devuelve una cadena con un espacio adicional tras cada letra.

    Args:
        texto (str): El texto de entrada.

    Returns:
        str: El texto con un espacio adicional tras cada letra.
    """
    texto_con_espacios = ' '.join(texto)
    return texto_con_espacios

def main():
    """
    Función principal que solicita al usuario un texto, convierte su espaciado
    y muestra el resultado.
    """
    texto = input("Ingrese un texto: ")  # Solicita al usuario que ingrese un texto
    texto_con_espaciado = ConvertirEspaciado(texto)  # Convierte el espaciado del texto
    print("Texto con espaciado adicional tras cada letra:")
    print(texto_con_espaciado)  # Muestra el resultado

if __name__ == "__main__":
    main()  # Llama a la función principal si se ejecuta este script como el programa principal
