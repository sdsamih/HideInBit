import cv2
from comparar import *

import hashlib
import random




def textToHash(text):
    text = str(text).encode('ascii')
    hash_object = hashlib.sha256(text)
    hash_bytes = hash_object.digest()

    return hash_bytes




def iterate(channel,senha): #receber o canal isolado

    rows=len(channel)
    columns = len(channel[0])

    positions= rows*columns

    hash_atual = textToHash(senha)

    for _ in range(10): #só um numero aleatorio, a verdadeira quantidade é a quantidade de bits da mensagem
        # Convertendo parte do hash para um número inteiro (exemplo: os primeiros 8 bytes)
        numero_gerado = int.from_bytes(hash_atual[:8], byteorder='big') % positions

        # Atualizando o hash para a próxima iteração
        hash_atual = textToHash(hash_atual)


        chosenrow = numero_gerado//columns

        chosencolumn= numero_gerado %columns

        print(f"\ncoordernada escolhida: {chosenrow};{chosencolumn} baseada no numero {numero_gerado} ")


#(bestRGBChannel("imagens/redbest.png")[1],"teste")

print(iterate(bestRGBChannel("imagens/redbest.png")[1],"teste"))