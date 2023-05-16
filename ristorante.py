diz_piatti = {'pasta':10.5,'pizza':6.0,'carne':15.5,'pesce':13.0}

class ordinazione():
    lista_ordine = [ ]
    spesa = 0
    persona = ''

ordinato = ordinazione()
def ordina_piatto(nome_piatto):
        if nome_piatto not in diz_piatti.keys():
            print('non abbiamo questo piatto')
        else:
            if len(ordinato.lista_ordine)>0:
                ordinato.lista_ordine.append([nome_piatto,diz_piatti[nome_piatto] ])   
                ordinato.spesa += diz_piatti[nome_piatto]
                #print(ordinato.lista_ordine)
            else:
                ordinato.lista_ordine = [[nome_piatto,diz_piatti[nome_piatto] ]]
                ordinato.spesa += diz_piatti[nome_piatto]  
                #print(ordinato.lista_ordine)  

def modifica_piatto(nome_piatto):
        print('Premi 1 per modificare il nome del piatto, 2 per modificare il prezzo, 3 per modificare entrambi')
        s = int(input())
        if s == 1:
            nome= input(('Inserisci il nuovo nome: '))
            diz_piatti[nome] = diz_piatti.pop(nome_piatto)
        elif s == 2:
            prezzo = float(input('inserisci il nuovo prezzo: '))
            diz_piatti[nome_piatto] = prezzo
        elif s == 3:
            nome= input(('Inserisci il nuovo nome: ')) 
            prezzo = float(input('inserisci il nuovo prezzo: ')) 
            diz_piatti[nome] = diz_piatti.pop(nome_piatto)
            diz_piatti[nome] = prezzo
        else:
            print('Errore')

def chiedi_il_conto():
        nome = input('dimmi il tuo nome')
        cognome = input('dimmi il tuo cognome')
        ordinato.persona = nome + ' ' + cognome
        print(f'ciao {ordinato.persona}')
        print('hai ordinato: ')
        for elemento in ordinato.lista_ordine:
            print(elemento[0])
        print(f' hai speso {ordinato.spesa}')  
        
  

def menu_interno(scelta):
    while scelta != 'esci':    
        if scelta == 'ordina':
            nome = input('inserisci il nome del piatto che vuoi ordinare')
            ordina_piatto(nome)
            scelta = input('inserisci una nuova scelta: ')        
        elif scelta == 'modifica':
            nome = input('inserisci il nome del piatto che vuoi modificare')
            modifica_piatto(nome)
            scelta = input('inserisci una nuova scelta: ') 
        elif scelta == 'conto':
            chiedi_il_conto()
            scelta = 'esci'
        elif scelta == 'esci':
            break
        else:
            return 'Errore'     

flag = True
while flag:
    print('se vuoi entrare premi 1,  per uscire premi 0')
    entrata_uscita = input()
    if entrata_uscita == '1':
        print('benvenuto')
        print('Fai la tua prima scelta tra ordina modifica conto e esci')   
        scelta = input()
        menu_interno(scelta)
        ordinato = ordinazione()

    elif entrata_uscita == '0':
        print('Arrivederci')
        flag = False             
    else:
         print('ERRORE')    