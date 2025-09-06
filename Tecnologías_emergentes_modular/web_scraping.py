import requests  # Importa requests para hacer peticiones HTTP
from bs4 import BeautifulSoup  # Permite parsear documentos HTML o XML para extraer datos

def scraping():
    """
    Realiza el parseo de los títulos de las películas más taquilleras de la historia
    """

    # URL del sitio a scrapear
    url = 'https://www.sensacine.com/noticias/cine/noticia-1000013021/'

    # Hacer la solicitud HTTP
    response = requests.get(url)

    ## response.text: Contiene el código HTML de la página obtenida con requests.
    ## BeautifulSoup(response.text, 'html.parser'):
    ## Parsear (analiza) el HTML y lo convierte en un objeto de BeautifulSoup.
    ## Facilita la navegación dentro del documento HTML.
    ## Permite buscar y extraer elementos con métodos como:
    ## .find(), .find_all(), .select(), etc.
    ## soup: Es el objeto que contiene el HTML ya procesado y listo para su manipulación.

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraer las películas referenciadas en la página filtrando por su etiqueta y clase
    for item in soup.find_all("h2", class_="bo-h2"):
        print(item.text)
if __name__ == "__main__":
    scraping()
