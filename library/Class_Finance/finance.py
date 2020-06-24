import csv
import requests
from unidecode import unidecode
import tkinter as tk


class Finance(object):

    def __init__(self, empresa):
        self.empresa = unidecode(empresa)
        self.lista_cod_empresas = []
        self.lista_dados = []

    def encontar_empresa(self):
        with open('library/Class_Finance/tabela.csv','r') as tabela:
             leitor = csv.reader(tabela, delimiter=',')
             for linha in leitor:
                 if self.empresa.lower() in str(linha).lower(): 
                    self.lista_cod_empresas.append(linha[1])
        
        lista_dados = []
        for i in self.lista_cod_empresas:
            try:
                dados = requests.get('http://168.138.234.162/api/v1/'+i).json()
                lista_dados.append(list(dados.items()))
            except:
                pass
        if lista_dados == []:
            return ("ERRO1997")

        popup = tk.Tk()
        popup.wm_title(self.empresa)
        popup.geometry( "300x400+800+80" )
        scrollbar = tk.Scrollbar(popup)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        list_categ = tk.Listbox(popup, yscrollcommand = scrollbar.set, background = "cyan", font="arial 10", highlightbackground= "yellow")
        for a in lista_dados:
            for i in a:
                list_categ.insert(tk.END, i[0]+" : "+i[1]) 
            list_categ.insert(tk.END, "  ") 
            list_categ.insert(tk.END, "  ")
        b1 = tk.Button(popup, text = "Fechar", command = popup.destroy, bg = "yellow", padx = 50)
        b1.pack(side = "bottom")
        list_categ.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
        scrollbar.config(command = list_categ.yview)
        popup.mainloop()

