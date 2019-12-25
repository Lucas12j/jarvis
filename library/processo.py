from library import Reconh_Voz_Google_Test, Reprod_Voz, wiki, datetime, cognition
import csv


class Processo(object):

    def __init__(self):
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
            self.soneca = True
        elif fala.lower() == 'acordar' and self.soneca == True:
            self.reproducao_voz("Desativando modo soneca")
            self.soneca = False
            self.check = False
        elif self.soneca == False:
            if str(fala) == 'ERRO1997':
                self.reproducao_voz("Não consegui te ouvir, por favor repita o que me disse.")
            elif str(fala) == 'pesquisar':
                self.reproducao_voz(" Sim senhor, me diga o que pesquisar")
                pesq_voz = Reconh_Voz_Google_Test.Captar_voz()
                wiki_pesq = wiki.Wiki(pesq_voz.captar_voz())
                self.reproducao_voz("Só um segundo.")
                print(wiki_pesq.pesquisar())
                self.reproducao_voz(wiki_pesq.pesquisar())
            elif str(fala) == 'data de hoje':
                self.reproducao_voz(dh.getData())
            elif str(fala) == 'hora':
                self.reproducao_voz(dh.getHora())
            else:
                a = cognition.Cognition(fala)
                self.reproducao_voz(a.decisao_resposta())
        else:
            pass

    def reproducao_voz(self, resposta):
        voz = Reprod_Voz.Reprod_Voz(str(resposta))
        voz.reproduzir()
