import cv2
from binaryoperations import *
from imageOperations import *

path="imagens/lenna.png"
message= "Texto daora pra testar"
senha="123"

image = cv2.imread(path)

insertBits(path,senha,message)

path2="imagens/lennaEncoded.png"
senha2="124"

mensagemExtraida = extractBits(path2,senha2)

print(mensagemExtraida)

