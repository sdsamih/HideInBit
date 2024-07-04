import cv2
import numpy as np
from binaryASCII import *

#Mensagem para binario com \0
texto="hello"
print(textToBin(texto))

#byte para caractere:
print(byteToText(textToBin(texto)[0:8]))
print(byteToText(textToBin(texto)[8:16]))
print(byteToText(textToBin(texto)[16:24]))
print(byteToText(textToBin(texto)[24:32]))

