import wikipedia
check = False

s = input("digite a busca : ")
wikipedia.set_lang('pt')
try:
    l = wikipedia.search(str(s), results=1, suggestion=False)
    print(wikipedia.summary(l, sentences=1, chars=0, auto_suggest= False))
    check = True
except:
    print("Houve um erro, tente uma pesquisa mais específica")
    check = True

if check == False:
    print("Perdão, mas não sei do que se trata essa pesquisa, por favor diga-me algo mais fácil.")