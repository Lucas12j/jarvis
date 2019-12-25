from library import Reconh_Voz_Google_Test, Reprod_Voz, wiki, datetime
import csv


class Processo(object):

    def __init__(self, dialogo):
        self.dialogo = dialogo
        #self.ativo = True
        self.soneca = False   
        self.check = False    

    def inicio(self):
        while True:
            if self.soneca == True and self.check == False:
                self.reproducao_voz("Ativando modo soneca.")
                self.check = True
            else:
                a = Reconh_Voz_Google_Test.Captar_voz()
                self.reconhecimento(a.captar_voz())

    def reconhecimento(self, fala):
        dh = datetime.Datetime()
        if fala.lower() == 'dormir':
            #self.ativo = False
            self.soneca = True
        elif fala.lower() == 'acordar' and self.soneca == True:
            self.reproducao_voz("Desativando modo soneca")
            #self.ativo = True
            self.soneca = False
            self.check = False

        elif self.soneca == False:
            with open(self.dialogo,'r', encoding='utf-8') as dialogo:
                reader = csv.reader(dialogo)
                for linha in reader:
                    if str(fala) == 'ERRO1997':
                        self.reproducao_voz("Não consegui te ouvir, por favor repita o que me disse.")
                        break
                    elif str(fala) == 'pesquisar':
                        self.reproducao_voz(" Sim senhor, me diga o que pesquisar")
                        pesq_voz = Reconh_Voz_Google_Test.Captar_voz()
                        wiki_pesq = wiki.Wiki(pesq_voz.captar_voz())
                        self.reproducao_voz("Só um segundo.")
                        print(wiki_pesq.pesquisar())
                        self.reproducao_voz(wiki_pesq.pesquisar())
                        break
                    elif str(fala) == 'data de hoje':
                        self.reproducao_voz(dh.getData())
                        break
                    elif str(fala) == 'hora':
                        self.reproducao_voz(dh.getHora())
                        break
                    else:
                        if linha[0].lower() == fala.lower():
                            self.reproducao_voz(linha[1])
                            break   
                        #Caso a fala do usuario não tenha confiabilidade suficiente, uma mensagem será enviando, explicando que não conseguiu ntender o que disse, e pedinmdo para dicionar mais no dialogos.csv                     
        else:
            pass
                    
    def reproducao_voz(self, resposta):
        voz = Reprod_Voz.Reprod_Voz(str(resposta))
        voz.reproduzir()