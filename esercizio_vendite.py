""" aggiungi la vendita di un prodotto    nome , quantità, prezzo 
    e poi stampare la quantità totale venduta per ogni prodotto    """
#SUGGERIMENTO:  vendite = {'nome': [prezzo , quantità]}

diz_vendite = {}

#aggiungere una vendita:
flag_vendita = True
while flag_vendita:
    scelta = input('1 per aggiungere, 0 per uscire ')
    if scelta == '1':
        nome = input('Inserire nome del prodotto: ')
        prezzo = float(input('Inserire prezzo del prodotto: '))
        quantita_venduta = int(input('Inserire quantità vendute: '))

        if nome not in diz_vendite:
            diz_vendite[nome]= [prezzo, quantita_venduta]
        else: 
            diz_vendite[nome][0] = prezzo             #aggiorno il prezzo
            diz_vendite[nome][1] += quantita_venduta    # sommo le quantità
    else:
        flag_vendita = False        
print(diz_vendite)        

# visualizzare il totale delle vendite per ogni prodotto
for chiave in diz_vendite.keys():
    print('Sono state vendute ',  diz_vendite[chiave][1],' quantità del prodotto ', chiave)