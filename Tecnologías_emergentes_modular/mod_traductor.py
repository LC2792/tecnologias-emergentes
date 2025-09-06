import requests  # Importa requests para hacer peticiones HTTP

def traductor(txt, lan, entrada=1):
    """
    Traduce un texto de español a otras lenguas y viceversa
    usando la API gratuita de MyMemory.

    Parámetros:
        txt (str): Mensaje para solicitar al usuario el texto a traducir.
        lan (str): Lenguaje como es|en, en|es, es|fr, fr|es, es|pt, pt|es, etc.
        entrada (int): 1 -> Pide texto por teclado. 0 -> Usa `txt` como texto a traducir.

    Retorna:
        str: Texto traducido.
    """
    try:
        # Entrada desde teclado o uso directo
        if entrada == 1:
            entrada = input(f"{txt}")
        else:
            entrada = txt

        # URL y parámetros de la API
        url = "https://api.mymemory.translated.net/get"
        params = {"q": entrada, "langpair": f"{lan}"}

        # Petición HTTP
        response = requests.get(url, params=params)

        # Procesar respuesta
        if response.status_code == 200:
            resultado = response.json()
            traduccion = resultado['responseData']['translatedText']
            return traduccion
        else:
            return "Error en la traducción: código HTTP " + str(response.status_code)

    except Exception as e:
        return f"Error en la solicitud: {e}"

if __name__ == "__main__":
    resultado = traductor("Escribe el texto que deseas traducir: ", "es|en", entrada=1)
    print("Traducción:", resultado)
