
menu = {}
ordini = []

flag_ = True
while flag_:
    scelta = input('''Premi 1 per aggiungere un piatto al menu, \n 2 per visualizzare il menu completo, \n 3 per cancellare un piatto dal menu,
                   4 prendere gli ordini, \n 5 fare il conto \n 6 per uscire''')
    if scelta == '6':
        flag_ = False
    elif  scelta == '1': 
        nome = input('inserisci il nome del piatto')
        prezzo = float(input('insrisci il prezzo del piatto'))  
        if nome not in menu.keys():
            menu[nome]= prezzo
        else:
            print('Piatto già esistente, voui aggiornare il prezzo?')  
            scelta_agg_prezzo = input('1 per aggiornare, 0 per uscire')
            if scelta_agg_prezzo == '1':
                menu[nome]= prezzo
    elif  scelta == '2':
        print(menu) 
    elif  scelta == '3': 
        nome_piatto = input('inserisci il nome del piatto da eliminare')
        if nome_piatto not in menu.keys():
            print('Il piatto inserito non esiste')
        else:
            del menu[nome_piatto]    
    elif  scelta == '4': 
        piatto = input('quale piatto vuoi ordinare? ')
        if piatto not in menu.keys():
            print('Non abbiamo questo piatto nel nostro menu')
        else:
            quantita = int(input('quanti ? '))
            ordini.append(piatto)
            ordini.append(quantita)    
    elif  scelta == '5': 
        conto = 0
        if len(ordini)==0:
            print('non hai ancora ordinato')
        else:
            for i in range(0,len(ordini),2):
                conto += ordini[i+1]*(menu[ordini[i]])
        print('ecco il conto: ', conto)        
    else:
        print('ERRORE!')
