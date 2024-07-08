import cv2
import numpy as np


def compararCanais():
    imagem = cv2.imread('lenna.png')
    blue, green, red = cv2.split(imagem)

    mediaBlue = np.mean(blue)
    mediaGreen = np.mean(green)
    mediaRed = np.mean(red)

    menor_media = min(mediaBlue, mediaGreen, mediaRed)

    if menor_media == mediaBlue:
        menor_media = "canal azul"
    elif menor_media == mediaGreen:
        menor_media = "canal verde "
    else:
        menor_media = "canal vermelho" 

    print(menor_media)
    return menor_media


#comparar = compararCanais()