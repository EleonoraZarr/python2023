import random

class Dado:
    def tira_un_dado(self):
        return random.randrange(1,21)

da = Dado()

flag = True
while flag:
    print('vuoi lanciare il dado?')  
    print('inserisci 1 per lanciare')  
    print('inserisci 0 per uscire') 
    scelta = input()
    if scelta == '0':
        print('Arrivederci')
        flag = False
    elif scelta == '1':
        print('è uscito: ',da.tira_un_dado())
    else:
        print('errore')        