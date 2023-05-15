"""
Esercizio calcolatrice PARTE 1
menu----> entra esci stampa  (3 calcoli)
       -----> mettere numeri 
       ----> fare somma sottrazione moltiplica
       -----> metti i risultati in un oggetto e stampali
       ---- oppure stampa la somma dei 3 risultati parziali"""

def somma(num1, num2):
    return num1+num2

def sottrazione(num1, num2):
    return num1-num2

def prodotto(num1, num2):
    return num1*num2


class Risultati_3:
    primo_risultato=0
    secondo_risultato=0
    terzo_risultato=0
    prima_op = ''
    seconda_op = ''
    terza_op = ''

flag_entra = True
check_conti = 0
while flag_entra:
    scelta = input('inserisci  0 per uscire, 1 per entrare e 2 per stampare')
    if scelta == '0':
        flag_entra = False
    elif scelta == '1': 
        check_conti = 1   
        num_calcoli = 0
        lista_risultati = Risultati_3()
        while num_calcoli < 3:
            num1= float(input('inserisci il primo numero'))
            num2= float(input('inserisci il secondo numero'))
            scelta_operazione = input('quale operazione vuoi fare? \n 1 per la somma 2 per la sottrazione e 3 per il prodotto: ')
            if scelta_operazione=='1':
                risultato = somma(num1,num2)
                operazione = 'somma'
                num_calcoli += 1
            elif scelta_operazione=='2':
                risultato = sottrazione(num1,num2)
                operazione = 'sottrazione'
                num_calcoli += 1
            elif scelta_operazione=='3':
                risultato = prodotto(num1,num2)
                operazione = 'prodotto'
                num_calcoli += 1
            else:
                print('scelta non accettata')  
            if num_calcoli==1:
                lista_risultati.primo_risultato = risultato
                lista_risultati.prima_op = operazione
            elif num_calcoli==2:
                lista_risultati.secondo_risultato = risultato
                lista_risultati.seconda_op = operazione
            elif num_calcoli==3:
                lista_risultati.terzo_risultato = risultato
                lista_risultati.terza_op = operazione
                print('La somma degli ultimi 3 calcoli è: ',lista_risultati.primo_risultato + lista_risultati.secondo_risultato + lista_risultati.terzo_risultato)
                
    elif scelta== '2': 
        if check_conti == 0:
            print('Non hai nulla da stampare')
        else:
            print('stampa risultati parziali: ',lista_risultati.prima_op, lista_risultati.primo_risultato,lista_risultati.seconda_op, lista_risultati.secondo_risultato,lista_risultati.terza_op, lista_risultati.terzo_risultato)
    else:
        print('ERRORE: valore non accettato')