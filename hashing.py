import cv2
import numpy as np

from comparar import *

import hashlib
import random




def textToHash(text):
    text = str(text).encode('ascii')
    hash_object = hashlib.sha256(text)
    hash_bytes = hash_object.digest()

    return hash_bytes




def iterate(caminho,senha): #iterar uma imagem baseado em uma senha, gerador de coordenadas que vai ser usado tanto para codificar quanto para decodificar

    channel = bestRGBChannel(caminho)[1]
    print(channel)


    rows=len(channel)
    columns = len(channel[0])

    occupiedMatrix = np.zeros([rows,columns], dtype="bool")


    positions= rows*columns

    hash_atual = textToHash(senha)

    while (True): #só um numero aleatorio, a verdadeira quantidade é a quantidade de bits da mensagem
        # Convertendo parte do hash para um número inteiro (exemplo: os primeiros 8 bytes)
        numero_original=int.from_bytes(hash_atual[8:16], byteorder='big')
        numero_gerado = (numero_original) % positions

        # Atualizando o hash para a próxima iteração
        hash_atual = textToHash(hash_atual)

        chosenrow = numero_gerado // columns
        chosencolumn = numero_gerado % columns

        while(occupiedMatrix[chosenrow][chosencolumn] == True): #tratamento de colisao (proxima posicao disponivel)

            numero_gerado= (numero_gerado+1)%positions

            chosenrow = numero_gerado // columns
            chosencolumn = numero_gerado % columns


        occupiedMatrix[chosenrow][chosencolumn]=True


       #print(f"\ncoordernada escolhida: {chosenrow};{chosencolumn} baseada no numero {numero_gerado} ")
        yield((chosenrow,chosencolumn))

coordGen = iterate("lenna.png","testefdsa")

print(next(coordGen)) # gerador de coordenada (usado para codificar e decodificar)
print(next(coordGen))
print(next(coordGen))
print(next(coordGen))
print(next(coordGen))
print(next(coordGen))
print(next(coordGen))
print(next(coordGen))
print(next(coordGen))
