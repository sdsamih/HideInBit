import numpy as np

#Transforma a mensagem a ser inserida em uma sequencia binaria (np.array)
#Automaticamente insere 0 \0 no final, para facilitar a extração
def textToBin( Asciitext):

    codedMessage = np.array([],dtype=np.bool_)


    for char in Asciitext:
        binary_code = bin(ord(char))[2:].zfill(8) #Caractere -> Ascii code -> Binario

        for bit in binary_code:
            codedMessage = np.append(codedMessage,bit=='1')

    for _ in range(8):
        codedMessage=np.append(codedMessage,False) #Adicionar o \0 no final da mensagem

    return codedMessage

#Quando for fazer a extração, os bit serão extraidos 1 por 1, toda vez que agrupar 8, passa essa funcao
#para transformar em letra
#Antes de chamar essa função, a extração precisa fazer a verificação se todos bits são 0 (fim da mensagem)

#Pode receber uma lista normal ou um np.array (melhor), mas sempre de tamanho 8
def byteToText( byte): #byte = array de 8 bools

    characterBin=""
    for  bit in byte:
        if (bit):
            characterBin += "1"
        else:
            characterBin += "0"


    asciiCode = int(characterBin,2)
    return chr(asciiCode)

def setLastBit(value,bit):
    mask = 0b00000001

    if bit== 1:
        newValue = value | mask #1
    else:
        newValue = value & ~ mask #0
    
    return newValue
