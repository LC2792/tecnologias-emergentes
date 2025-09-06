from utilidades import clrscr, getch

def main():
    while True:
        clrscr()
        option = input("Seleccione una opción:\n"
                       "Tecnologías emergentes y disruptivas\n"
                       "1 -> Web scraping\n"
                       "2 -> Traducir texto\n"
                       "3 -> Generar imagen\n"
                       "4 -> Audio a texto\n"
                       "5 -> Texto a audio\n"
                       "6 -> Procesamiento del lenguaje natural\n"
                       "7 -> Generar texto\n"
                       "8 -> Blockchain\n"
                       "9 -> Codigos QR\n"
                       "10 -> Realidad aumentada\n"
                       "0 -> Salir\n"
                       "Opción: ").strip()

        match option:
            case '1':
                from web_scraping import scraping
                scraping()
                getch()
            case '2':
                from operaciones_texto import traducir
                traducir()
                getch()
            case '3':
                from generar_imagen import generar_imagen
                generar_imagen()
                getch()
            case '4':
                from operaciones_texto import audio_to_text
                audio_to_text()
                getch()
            case '5':
                from operaciones_texto import text_to_audio
                texto = input("Digite el texto a convertir: ")
                text_to_audio(texto)
                getch()
            case '6':
                from operaciones_texto import traductor_nlp
                texto = input("Digite el texto a convertir: ")
                traductor_nlp(texto)
                getch()
            case '7':
                from operaciones_texto import gen_text
                gen_text()
                getch()
            case '8':
                from blockchain import cadena_bloques
                cadena_bloques()
                getch()
            case '9':
                from codigos_qr import menu_qr
                menu_qr()
                getch()
            case '10':
                from realidad_aumentada import menu_ar
                menu_ar()
                getch()
            case '0':
                print("bye")
                getch()
                break
            case _:
                print("Seleccione opción válida")
                getch()

if __name__ == '__main__':
    main()
