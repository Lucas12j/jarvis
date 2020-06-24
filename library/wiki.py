import wikipedia

class Wiki():

    def __init__(self, pesq_usuario):
        self.pesq_usuario = pesq_usuario
        self.check  = False
        if self.pesq_usuario != 'ERRO1997':
            print("Pesquisando na minha base de dados por: "+ self.pesq_usuario+ " ...")
    

    def pesquisar(self):
        wikipedia.set_lang('pt')
        try:
            l = wikipedia.search(str(self.pesq_usuario), results=1, suggestion=False)
            return wikipedia.summary(l, sentences=1, chars=0, auto_suggest= False)
            
        except:
            return "Perdão, mas não sei do que se trata essa pesquisa, por favor diga-me algo mais fácil."
            
