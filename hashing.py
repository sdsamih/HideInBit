import cv2
import numpy as np

from comparar import *
from binaryASCII import *

import hashlib
import random



def setLastBit(value,bit):
    mask = 0b00000001

    if bit== 1:
        newValue = value | mask #1
    else:
        newValue = value & ~ mask #0
    
    return newValue

def textToHash(text):
    text = str(text).encode('ascii')
    hash_object = hashlib.sha256(text)
    hash_bytes = hash_object.digest()

    return hash_bytes




def iterate(channel,senha): #iterar uma imagem baseado em uma senha, gerador de coordenadas que vai ser usado tanto para codificar quanto para decodificar


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


def insertBits(path,senha,message):

    bits=textToBin(message)
    
    nameChannel,chosenchannel = bestRGBChannel(path)

    image = cv2.imread(path)
    
    blue,green,red = cv2.split(image)


    coordGen=iterate(chosenchannel,senha)

    for bit in bits:
        coords=next(coordGen)
        row=coords[0]
        column=coords[1]
        print(f"{bit} vai ser inserido em {row,column}")

        if(bit):
            chosenchannel[row][column] = ((chosenchannel[row][column]) | 1)
        else:
            chosenchannel[row][column] = (chosenchannel[row][column] & 254)
    

    if nameChannel=="blue":
        codedImage=cv2.merge((chosenchannel,green,red))
    elif nameChannel=="red":
        codedImage=cv2.merge((blue,green,chosenchannel))
    else:
        codedImage=cv2.merge((blue,chosenchannel,red))
    
    
    return codedImage



