"""
Esercizio calcolatrice PARTE 2
menu----> entra esci stampa pulisci (3 calcoli)
       -----> mettere numeri 
       ----> fare somma sottrazione moltiplica
       -----> metti i risultati in un oggetto e stampali  
       ---- oppure stampa tutti i risultati  3 a 3 
       ------ elimina lo storico risultati """

def somma(num1, num2):
    return num1+num2

def sottrazione(num1, num2):
    return num1-num2

def prodotto(num1, num2):
    return num1*num2

class Risultati():
    def __init__(self,primo_risultato,secondo_risultato,terzo_risultato):
        self.primo_risultato = primo_risultato
        self.secondo_risultato = secondo_risultato
        self.terzo_risultato = terzo_risultato

flag_entra = True
check_conti = 0
lista_totale = []

while flag_entra:
    scelta = input('inserisci  0 per uscire, 1 per entrare e 2 per stampare 3 per eliminare lo storico')
    if scelta == '0':
        flag_entra = False
    elif scelta == '1': 
        check_conti = 1   
        num_calcoli = 0
        lista_risultati = Risultati()
        while num_calcoli < 3:
            num1= float(input('inserisci il primo numero'))
            num2= float(input('inserisci il secondo numero'))
            scelta_operazione = input('quale operazione vuoi fare? \n 1 per la somma 2 per la sottrazione e 3 per il prodotto: ')
            if scelta_operazione=='1':
                risultato = somma(num1,num2)
                num_calcoli += 1
            elif scelta_operazione=='2':
                risultato = sottrazione(num1,num2)
                num_calcoli += 1
            elif scelta_operazione=='3':
                risultato = prodotto(num1,num2)
                num_calcoli += 1
            else:
                print('scelta non accettata')  
            if num_calcoli==1:
                lista_risultati.primo_risultato = risultato
            elif num_calcoli==2:
                lista_risultati.secondo_risultato = risultato
            elif num_calcoli==3:
                lista_risultati.terzo_risultato = risultato
                print('La somma degli ultimi 3 calcoli è: ',lista_risultati.primo_risultato + lista_risultati.secondo_risultato + lista_risultati.terzo_risultato)
                lista_totale.append(lista_risultati)
    elif scelta== '2': 
        if check_conti == 0:
            print('Non hai nulla da stampare')
        else:
            cosa_stampare = input('per stampare tutto premi 1, per stampare solo le ultime 3 premere 2')
            if cosa_stampare == '1':
                print('stampa : ',lista_totale)
            elif cosa_stampare == '2':
                print('gli ultimi 3 sono: ',lista_totale[-3],lista_totale[-2],lista_totale[-1])
            else:
                print('scelta non accettata')    
    elif scelta == '3':  
        lista_totale = []
        check_conti = 0      
    else:
        print('ERRORE: valore non accettato')        