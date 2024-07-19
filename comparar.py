import cv2
import numpy as np

def bestRGBChannel(caminho): #passar o caminho da imagem
    imagem = cv2.imread(caminho)
    blue, green, red = cv2.split(imagem)

    mediaBlue = np.mean(blue)
    mediaGreen = np.mean(green)
    mediaRed = np.mean(red)

    menor_media = min(mediaBlue, mediaGreen, mediaRed)


    if menor_media == mediaBlue:
        return ("blue", blue)
    elif menor_media == mediaGreen:
        return ("green", green)
    else:
        return ("red", red)
