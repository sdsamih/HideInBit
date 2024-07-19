import cv2
import numpy as np
from binaryASCII import *
from comparar import *
from hashing import *
#from comparar import compararCanais

# Mensagem para binario com \0

#verCanal = compararCanais()
#print(verCanal)


path="lenna.png"
message= "a"
senha="123"

image1 = cv2.imread(path)
imagem_codificada = insertBits(path,senha,message)



height, width, _ = image1.shape

# Percorrer cada pixel das imagens e exibir coordenadas diferentes
for x in range(height):
    for y in range(width):
        if not np.array_equal(image1[x, y], imagem_codificada[x, y]):
            print(f"Coordenada diferente: ({x}, {y}) - Image1: {image1[x, y]} - imagem_codificada: {imagem_codificada[x, y]}")

# Exibir as imagens para referência
cv2.imshow('Imagem 1', image1)
cv2.imshow('Imagem 2', imagem_codificada)
cv2.waitKey(0)
cv2.destroyAllWindows()









#print(textToBin(texto))
# byte para caractere:
#print(byteToText(textToBin(texto)[0:8]))
#print(byteToText(textToBin(texto)[8:16]))
#print(byteToText(textToBin(texto)[16:24]))
#print(byteToText(textToBin(texto)[24:32]))



