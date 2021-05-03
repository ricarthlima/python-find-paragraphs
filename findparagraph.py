import os
import io

PEQUENO = 200
MEDIO = 400
GRANDE = 700

espacoBusca = MEDIO

print("Bem vindo ao buscador de termos! \n")
while True:
    escolha = input("1- Decida o tamanho do paragrafo que será buscado:\n(PEQUENO, MEDIO ou GRANDE)\n>>> ").upper()
    if escolha == 'PEQUENO':
        espacoBusca = PEQUENO
        break
    elif escolha == 'GRANDE':
        espacoBusca = GRANDE
        break
    elif escolha == 'MEDIO':
        espacoBusca = MEDIO
        break

listWords = []
while True:
    word = input("\n2- Insira uma palavra de busca: (STOP para parar)\n>>> ")
    if word == "STOP" or word == "":
        break
    else:
        listWords.append(word.lower())

print("\n3- Agora vamos anexar os arquivos, certifique-se que estão todos na pasta 'anexo'")
input("Continuar?")

listFiles = []

arrayDirs = os.listdir("anexos")
if "results" not in os.listdir():
    os.mkdir("results")

i = 0
while i < len(arrayDirs):
    file = io.open("anexos/" + arrayDirs[i],mode="r", encoding="utf-8")
    text = file.read().lower()
    file.close()

    listFiles.append((arrayDirs[i], text))
    i += 1

print("\n4- Arquivos anexados, vamos começar as buscas!")
input("Continuar?")

extensao = "txt"

while True:
    print("\n5- Mas antes, qual extensão de saída você prefere? TXT ou MD?")
    escolha = input(">>> ").lower()
    if escolha in ["txt","md"]:
        extensao = escolha
        break
    

i = 0
while i < len(listFiles):
    output = ""
    path = listFiles[i][0]
    text = listFiles[i][1]
    
    for word in listWords:
        startIndex = 0
        while True:
            index = text.find(word, startIndex)
            if index == -1:
                break
            else:
                startIndex = index + 1
                
                output += text[index-espacoBusca:index-1]
                output += " **"
                output += text[index:index+len(word)]
                output += "** "
                output += text[index+len(word):index+espacoBusca]
                output += "\n\n\n\n\n\n\n\n\n\n\n\n"
        
    if output != "":
        file = io.open("results/" + path[:-3] + extensao, mode = "w", encoding = "utf-8")
        file.write(output)
        file.close()
    i += 1
print("\nFIM- Arquivos gerados")
input()
    
