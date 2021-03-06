import csv
import random

class Cognition(object):

    def __init__(self, frase):
        self.frase = frase
        self.lista_palavras = []
        self.lista_porcentagem = []
        self.palavra = ''

    def separa_palavra(self):
        for i in self.frase:
            if i != ' ':
                self.palavra = self.palavra+str(i)
            else:
                self.lista_palavras.append(self.palavra)
                self.palavra = ''
        self.lista_palavras.append(self.palavra)
        self.calcular()
    
    def calcular(self):
        porcent = 0
        with open('Dialogos.csv' ,'r', encoding='utf-8') as dialogo:
            reader = csv.reader(dialogo)
            for frase_dialogo in reader:
                for palavra in self.lista_palavras:
                    if palavra.lower() in frase_dialogo[0].lower():
                        porcent += 1
                self.lista_porcentagem.append(float(porcent/ len(self.lista_palavras)))
                porcent = 0
        self.decisao()

    def decisao(self):
        maior = 0
        lista_index = []
        index = 0
        aux = 0
        
        for i in self.lista_porcentagem:
            if i > maior:
                maior = i

        if maior >= 0.5:

            for i in self.lista_porcentagem:
                if i == maior:
                    lista_index.append(index)
                index += 1
            aleatorio = random.randint(0, len(lista_index)-1)
            print(f'aleatorio : {aleatorio}')
            print(self.lista_porcentagem)
            print(lista_index[aleatorio])

            with open('Dialogos.csv' ,'r', encoding='utf-8') as dialogo:
                reader = csv.reader(dialogo)
                for i in reader:
                    if aux == lista_index[aleatorio]:
                        print(i[0])
                        break
                    else:
                        aux += 1
        else:
            print("Não entendi o que me disse, adicione vocabulário no meu arquivo Dialogos.csv")
        

    
a = Cognition('onde você mora')
a.separa_palavra()


#implementar grau de confiabilidade