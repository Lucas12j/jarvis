from library import Reconh_Voz_Google_Test, Reprod_Voz, wiki, datetime
import csv


class Processo(object):

    def __init__(self, dialogo):
        self.dialogo = dialogo
        self.dh = datetime.Datetime()
        self.ativo = True
        self.soneca = False       

    def inicio(self):

        while True:
            if self.ativo == False and self.soneca == False:
                self.reproducao_voz("Ativando modo soneca.")
                self.soneca = True
            else:
                a = Reconh_Voz_Google_Test.Captar_voz()
                self.reconhecimento(a.captar_voz())

        
    def reconhecimento(self, fala):
        if fala.lower() == 'dormir':
            self.ativo = False
        elif fala.lower() == 'acordar' and self.ativo == False:
            self.reproducao_voz("Desativando modo soneca")
            self.ativo = True
            self.soneca = False
        elif self.ativo == True and self.soneca == False:
            check = False
            with open(self.dialogo,'r', encoding='utf-8') as dialogo:
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
        else:
            pass
                    
    def reproducao_voz(self, resposta):
        voz = Reprod_Voz.Reprod_Voz(str(resposta))
        voz.reproduzir()