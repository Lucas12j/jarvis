from library import processo
import csv

while True:
    #start = processo.Processo('E:\Projetos\Jarvis\Dialogos.csv')   #(Para Windows) Coloque o local do arquivo "Dialogo.csv" dentro argumento.
    start = processo.Processo('Dialogos.csv')                     #(Outros S.Os)  Aqui não é necessário.           
    start.inicio()
    
     
#OBS: Ao usar no windows, atenção na escrita da base de dados do dialogo, pois não é aceito caracteres como acentos e "ç", será necessário mudar a
