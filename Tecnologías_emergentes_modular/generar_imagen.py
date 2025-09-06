from PIL import Image  # Librería Pillow para manipulación de imágenes
import torch           # PyTorch, que se usa para modelos de IA
from diffusers import StableDiffusionPipeline  # Librería diffusers para usar modelos de difusión
from mod_traductor import traductor  # Librería local para traducir un texto

def generar_imagen():
    """
    Genera una imagen a partir de una descripción en español usando el modelo Stable Diffusion.

    Esta función:
    1. Carga el modelo "Stable Diffusion v1-5" desde Hugging Face.
    2. Traduce el texto ingresado por el usuario de español a inglés.
    3. Usa el modelo de IA para generar una imagen basada en el texto traducido.
    4. Guarda la imagen generada en un archivo llamado "output.png".
    5. Muestra la imagen en pantalla.

    Manejo de errores:
    - Si la traducción falla, usa el texto en español directamente.
    - Si la carga del modelo falla, muestra un mensaje de error.
    - Si la generación de la imagen falla, captura la excepción.
    """

    try:
        print("Cargando el modelo de Stable Diffusion, esto puede tardar un momento...")
        pipeline = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32  # Optimiza el uso de memoria
        )

        # Mover el modelo a GPU si está disponible
        device = "cuda" if torch.cuda.is_available() else "cpu"
        pipeline.to(device)

        # Solicitar la descripción al usuario y traducirla
        prompt = traductor("Describa la imagen que desea generar:", "es|en")

        print("🖼️ Generando la imagen, por favor espere...")
        image = pipeline(prompt).images[0]

        # Guardar la imagen en un archivo
        output_path = "output.png"
        image.save(output_path)
        print(f"✅ Imagen generada y guardada en {output_path}")

        # Mostrar la imagen generada
        image.show()

    except Exception as e:
        print(f"❌ Error al generar la imagen: {e}")
if __name__ == "__main__":
    generar_imagen()
