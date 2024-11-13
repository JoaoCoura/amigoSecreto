#Biblioteca para sorteio
import random

x = int(input("Numero de amigos: "))
amigos = []
sorteios = {}

#Coleta dos nomes
for i in range(x):
    amigo = input(f"Amigo {i+1}: ")
    amigos.append(amigo)

amigos_sorteados = amigos.copy()

for amigo in amigos:
    while True:
        pessoa_sorteada = random.choice(amigos_sorteados)
        #verificacao para a pessoa não se autosortear e a pessoa a qual for sorteada nao ter sorteado ela (presente um pro outro)
        if pessoa_sorteada != amigo and (pessoa_sorteada not in sorteios or amigo != sorteios[pessoa_sorteada]):
            break
    
    #adiciona no dicionario
    sorteios[amigo] = pessoa_sorteada
    #remove da lista de nomes a serem sorteados
    amigos_sorteados.remove(pessoa_sorteada)

for amigo, pessoa_sorteada in sorteios.items():
    print(f"{amigo} tirou {pessoa_sorteada}")