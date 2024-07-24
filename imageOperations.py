import cv2
import numpy as np
from binaryoperations import *
import hashlib
import os

def bestRGBChannel(path): #passar o caminho da imagem
    print(f" escolhendo o canal de {path}")
    imagem = cv2.imread(path)
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

    while (True): 
        # Convertendo parte do hash para um número inteiro (escolhe o segundo byte)
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

import os
import cv2

def insertBits(path, senha, message):
    bits = textToBin(message)
    
    nameChannel, chosenchannel = bestRGBChannel(path)

    image = cv2.imread(path)
    
    blue, green, red = cv2.split(image)

    coordGen = iterate(chosenchannel, senha)

    for bit in bits:
        coords = next(coordGen)
        row = coords[0]
        column = coords[1]

        if bit:
            chosenchannel[row][column] = ((chosenchannel[row][column]) | 1)
        else:
            chosenchannel[row][column] = (chosenchannel[row][column] & 254)

    if nameChannel == "blue":
        codedImage = cv2.merge((chosenchannel, green, red))
    elif nameChannel == "red":
        codedImage = cv2.merge((blue, green, chosenchannel))
    else:
        codedImage = cv2.merge((blue, chosenchannel, red))

    fileName = os.path.basename(path)
    fileName, extension = os.path.splitext(fileName)

    encoded_image_path = os.path.join(os.path.dirname(path), f"{fileName}Encoded.png")
    cv2.imwrite(encoded_image_path, codedImage)

    return encoded_image_path


def extractBits(path,senha):

    mensagem=""
    codedChannel = bestRGBChannel(path)[1]

    coordGen= iterate(codedChannel,senha)

    while True:
        bitsBuffer= np.array([],dtype=np.bool_) #cria um buffer de 1 byte pro caractere

        for index in range (8): 

            x,y = next(coordGen)
            bit = ((codedChannel[x][y]) %2 != 0) #par = ultimo bit 0, impar = ultimo bit 1
            
            bitsBuffer=np.append(bitsBuffer,bit) #preencher o buffer de caractere
        
        caractere=byteToText(bitsBuffer) #consome o buffer
        mensagem += caractere 

        if caractere=="\0": #se 00000000, acaba
            return mensagem





