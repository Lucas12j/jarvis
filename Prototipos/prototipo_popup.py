import tkinter as tk
import requests

dados = requests.get('http://168.138.234.162/api/v1/itsa4').json()
lista_dados = list(dados.items())
popup = tk.Tk()
popup.wm_title("teste")
popup.geometry( "300x400+800+80" )
scrollbar = tk.Scrollbar(popup)
scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
list_categ = tk.Listbox(popup, yscrollcommand = scrollbar.set, background = "cyan", font="arial 10", highlightbackground= "yellow")
for i in lista_dados:
    list_categ.insert(tk.END, i[0]+" : "+i[1]) 
    print("\n")
b1 = tk.Button(popup, text = "Fechar", command = popup.destroy, bg = "yellow", padx = 50)
b1.pack(side = "bottom")
list_categ.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
scrollbar.config(command = list_categ.yview)

popup.mainloop()