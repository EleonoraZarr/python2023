
menu = {}
ordini = []

flag_ = True
while flag_:
    scelta = input('''Premi 1 per aggiungere un piatto al menu, \n 2 per visualizzare il menu completo, \n 3 per cancellare un piatto dal menu,
                   4 prendere gli ordini, \n 5 fare il conto \n 6 per uscire''')
    if scelta == '6':                                                                #esco da tutto
        flag_ = False
    elif  scelta == '1':                                                  
        nome = input('inserisci il nome del piatto')
        prezzo = float(input('insrisci il prezzo del piatto'))  
        if nome not in menu.keys():                                                #se non c'è lo inserisco
            menu[nome]= prezzo
        else:
            print('Piatto già esistente, voui aggiornare il prezzo?')  
            scelta_agg_prezzo = input('1 per aggiornare, 0 per uscire')            # se già c'è chiedo se vuole aggiornare il prezzo
            if scelta_agg_prezzo == '1':
                menu[nome]= prezzo
    elif  scelta == '2':                                                          #stampo il menu completo (come dizionario)
        print(menu) 
    elif  scelta == '3': 
        nome_piatto = input('inserisci il nome del piatto da eliminare')
        if nome_piatto not in menu.keys():
            print('Il piatto inserito non esiste')
        else:
            del menu[nome_piatto]                                                  #elimino il piatto dal menu
    elif  scelta == '4':
        ord_flag = True
        while ord_flag:                                                         # per ordinare piu piatti senza tornare al menu principale
            piatto = input('quale piatto vuoi ordinare? ')
            if piatto not in menu.keys():
                print('Non abbiamo questo piatto nel nostro menu')
            else:
                quantita = int(input('quanti ? '))
                ordini.append(piatto)                                             # aggiungo alla lista ordini il piatto ordinato e la quantità
                ordini.append(quantita)  
            continua_ordine=input('0 per uscire 1 per ordinare un altro piatto') 
            if continua_ordine==0:
                ord_flag=False                                                   # quando ho finito l'ordine esco    
    elif  scelta == '5': 
        conto = 0
        if len(ordini)==0:
            print('non hai ancora ordinato')
        else:
            for i in range(0,len(ordini),2):                                    # nella lista ordini ho piatto, quantità, piatto, quantità.....
                conto += ordini[i+1]*(menu[ordini[i]])                          #dal menu vedo il prezzo
        print('ecco il conto: ', conto)        
    else:
        print('ERRORE!')
