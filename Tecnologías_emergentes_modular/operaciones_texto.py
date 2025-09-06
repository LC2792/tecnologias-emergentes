from transformers import pipeline  # Modelos NLP (traducción, texto, etc.)
import pyttsx3  # Texto a voz offline
from mod_traductor import traductor  # Función local para traducción básica


def gen_text():
    """
    Traduce un texto del español al inglés, genera una continuación con GPT-2,
    y traduce el resultado de nuevo al español.
    """
    texto = traductor("Digite el texto base :", "es|en")
    
    generador = pipeline("text-generation", model="gpt2")
    resultado = generador(texto, max_length=250, num_return_sequences=1, truncation=True)
    Texto_generado = resultado[0]['generated_text']

    print("\nTexto generado en español:", traductor(Texto_generado[:500], "en|es", 0))


def traductor_nlp(texto):
    """
    Traduce un texto del español al inglés usando un modelo neuronal preentrenado.
    """
    traductor_model = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")
    texto_en = traductor_model(texto)[0]["translation_text"]
    print("Traducción:", texto_en)


def text_to_audio(texto):
    """
    Convierte texto a audio y guarda el resultado como output.wav.
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    engine.save_to_file(texto, "output.wav")
    engine.runAndWait()
    print("Audio generado: output.wav")


def audio_to_text():
    """
    Convierte un archivo de audio a texto usando Whisper de Hugging Face.
    """
    stt = pipeline("automatic-speech-recognition", model="openai/whisper-small")
    audio_path = "audio.mp3"  # Reemplaza con la ruta de tu archivo
    resultado = stt(audio_path)
    print("Texto transcrito:", resultado["text"])


def traducir():
    """
    Menú interactivo para traducir entre varios idiomas usando la función `traductor`.
    """
    texto = "Introduzca el texto a traducir:"
    while True:
        lang = input("Seleccione una operación:\n"
                     "1 -> Español a inglés\n"
                     "2 -> Inglés a español\n"
                     "3 -> Español a portugués\n"
                     "4 -> Portugués a español\n"
                     "5 -> Español a italiano\n"
                     "6 -> Italiano a español\n"
                     "7 -> Español a francés\n"
                     "8 -> Francés a español\n"
                     "0 -> Salir\n"
                     "Opción: ").strip()
        
        if lang == '1':
            l = "es|en"
        elif lang == '2':
            l = "en|es"
        elif lang == '3':
            l = "es|pt"
        elif lang == '4':
            l = "pt|es"
        elif lang == '5':
            l = "es|it"
        elif lang == '6':
            l = "it|es"
        elif lang == '7':
            l = "es|fr"
        elif lang == '8':
            l = "fr|es"
        elif lang == '0':
            print("Fin traductor")
            break
        else:
            print("Seleccione una opción válida")
            continue
        
        print(traductor(texto, l))
if __name__ == "__main__":
    # Ejemplo: probar la función traducir directamente
    traducir()
