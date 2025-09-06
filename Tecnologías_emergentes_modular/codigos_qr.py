import qrcode
import cv2
import numpy as np

def generar_qr():
    """
    Genera un código QR a partir de un texto o URL ingresado por el usuario.
    El archivo se guarda como 'codigo_qr.png' y se muestra en una ventana.
    """
    data = input("Ingrese el texto o URL para generar el código QR: ")
    qr = qrcode.make(data)
    qr.save("codigo_qr.png")
    print("Código QR guardado como 'codigo_qr.png'")

    # Mostrar con OpenCV
    img = cv2.imread("codigo_qr.png")
    if img is not None:
        cv2.imshow("Código QR", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error al cargar la imagen del código QR.")

def leer_qr():
    """
    Lee un código QR desde la cámara (requiere una buena iluminación y enfoque).
    Muestra el contenido detectado por consola.
    """
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)
        if bbox is not None:
            cv2.polylines(frame, [np.int32(bbox)], True, (255, 0, 0), 2)
            if data:
                print("Código QR detectado:", data)
                cv2.putText(frame, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Escáner QR", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def menu_qr():
    """
    Muestra un menú interactivo para generar o leer códigos QR.
    """
    while True:
        opcion = input("\nCódigo QR - Seleccione una opción:\n"
                       "1 -> Generar código QR\n"
                       "2 -> Leer código QR desde cámara\n"
                       "0 -> Volver\n"
                       "Opción: ").strip()
        
        if opcion == '1':
            generar_qr()
        elif opcion == '2':
            leer_qr()
        elif opcion == '0':
            print("Saliendo del módulo QR.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    menu_qr()
