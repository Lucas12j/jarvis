from library import Reconh_Voz_Google_Test, Reprod_Voz, wiki, datetime
import csv

class Processo(object):

    def __init__(self, dialogo):
        self.dialogo = dialogo
        self.dh = datetime.Datetime()
        
        

    def inicio(self):
    
        a = Reconh_Voz_Google_Test.Captar_voz()
        self.reconhecimento(a.captar_voz())

        
    def reconhecimento(self, fala):
        check = False

        with open(self.dialogo, 'r') as dialogo:
            reader = csv.reader(dialogo)
            for linha in reader:
                if str(fala) == 'ERRO1997' and check !=True:
                     self.reproducao_voz("Não consegui te ouvir, por favor repita o que me disse.")
                     check = True
                elif str(fala) == 'pesquisar' and check != True:
                    self.reproducao_voz(" Sim senhor, me diga o que pesquisar")
                    pesq_voz = Reconh_Voz_Google_Test.Captar_voz()
                    wiki_pesq = wiki.Wiki(pesq_voz.captar_voz())
                    self.reproducao_voz("Só um segundo.")
                    print(wiki_pesq.pesquisar())
                    self.reproducao_voz(wiki_pesq.pesquisar())
                    check = True
                elif str(fala) == 'data de hoje' and check != True:
                    self.reproducao_voz(self.dh.getData())
                    check = True
                elif str(fala) == 'hora' and check != True:
                    self.reproducao_voz(self.dh.getHora())
                    check = True
                else:
                    if linha[0].lower() == fala.lower() and check != True:
                        self.reproducao_voz(linha[1])
                        check = True
            if check == False:   
                print("Perdão, não compreendi o que me disse, me ensine adicionando vocabulários no arquivo Dialogos.csv")
                
    def reproducao_voz(self, resposta):
        voz = Reprod_Voz.Reprod_Voz(str(resposta))
        voz.reproduzir()
        




























'''
        if str(a.captar_voz()) == 'Lucas':
            print("Olá meu senhor")
        else:
            print(a.captar_voz())
'''
