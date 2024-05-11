import os
import time

def maquinaEscrever(texto:str,tempo:float):
    os.system("cls")
    for letra in texto:
        print(letra, end="",flush=True)
        time.sleep(tempo)

        