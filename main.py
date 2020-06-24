from library import processo
import threading
import pyglet
import os

i = 0
#CONSEGUI FAZER O JARVIS TRABALHAR PARALELAMENTE COM A ANIMAÇÃO.
#ARRUMAR FUNÇÃO MAIN, E TAMBÉM MELHORAR A ANIMAÇÃO


def main():
    start = processo.Processo()                         
    start.inicio()

def animacao():
    pass


t1 = threading.Thread(target=main)
t2 = threading.Thread(target=animacao)

t1.start()
t2.start()



    
    
