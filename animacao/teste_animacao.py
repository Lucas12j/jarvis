import os

os.system('clear')
for i in range(0,10):
    
    with open("animacao1.txt","r") as animacao:
        for i in animacao:
            print(i.replace("\n",""))

    os.system('sleep 0.5')
    os.system('clear')

    with open("animacao2.txt","r") as animacao:
        for i in animacao:
            print(i.replace("\n",""))

    os.system('sleep 0.5')
    os.system('clear')

    with open("piscar.txt","r") as animacao:
        for i in animacao:
            print(i.replace("\n",""))

    os.system('sleep 0.5')
    os.system('clear')