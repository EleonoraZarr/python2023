diz_piatti = {'pasta':10.5,'pizza':6.0,'carne':15.5,'pesce':13.0}

class ordinazione:
    lista_ordine = [ ]
    spesa = 0
    def pulisci_ordine(self):
        self.lista_ordine = []
        self.spesa = 0


class Utente:
    def crea_profilo(self):
        nome = input('dimmi il tuo nome')
        cognome = input('dimmi il tuo cognome')
        persona = nome + ' ' + cognome  
        return persona
    ordine = ordinazione()
    def ordina_piatto(self,nome_piatto):
        if nome_piatto not in diz_piatti.keys():
            print('non abbiamo questo piatto')
        else:
            if len(self.ordine.lista_ordine)>0:
                self.ordine.lista_ordine.append([nome_piatto,diz_piatti[nome_piatto] ])   
                self.ordine.spesa += diz_piatti[nome_piatto]
                #print(ordinato.lista_ordine)
            else:
                self.ordine.lista_ordine = [[nome_piatto,diz_piatti[nome_piatto] ]]
                self.ordine.spesa += diz_piatti[nome_piatto]  
                #print(ordinato.lista_ordine)

    def chiedi_il_conto(self):
        print('hai ordinato: ')
        for elemento in self.ordine.lista_ordine:
            print(elemento[0])
        print(f' hai speso {self.ordine.spesa}')    

cliente = Utente()
def menu_cliente(scelta):
    while scelta != 'esci':    
        if scelta == 'ordina':
            nome = input('inserisci il nome del piatto che vuoi ordinare')
            cliente.ordina_piatto(nome)
            scelta = input('inserisci una nuova scelta: ')        
        elif scelta == 'conto':
            cliente.chiedi_il_conto()
            cliente.ordine.pulisci_ordine()
            scelta = 'esci'
        elif scelta == 'esci':
            cliente.ordine.pulisci_ordine()
            break
        else:
            return 'Errore'  
        
class Manager:
    def aggiungi_piatto_nel_dizionario(self):
        nome = input('quale piatto vuoi aggiungere: ')  
        if nome in diz_piatti.keys():
            print('piatto già presente nel menù ')
        else:    
            prezzo = float(input('con che prezzo? '))  
            diz_piatti[nome] = prezzo   

    def elimina_piatto_dal_dizionario(self):
        nome = input('quale piatto vuoi eliminare: ')  
        if nome not in diz_piatti.keys():
            print('il piatto digitato non è presente nel menù ')
        else:      
            del diz_piatti[nome]   

    def modifica_piatto(self,nome_piatto):
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

    def visualizza_menu(self):
        print('il menu completo è: ')
        print(diz_piatti)        

man = Manager()
def menu_manager(scelta):
    while scelta != 'esci':    
        if scelta == 'aggiungi':
            man.aggiungi_piatto_nel_dizionario()
            scelta = input('inserisci una nuova scelta: ')        
        elif scelta == 'elimina':
            man.elimina_piatto_dal_dizionario()
            scelta = input('inserisci una nuova scelta: ')
        elif scelta == 'modifica':
            nome = input('inserisci il nome del piatto da modificare')
            if nome in diz_piatti.keys():
                man.modifica_piatto(nome)
            else:
                print('piatto non presente nel menù ')    
            scelta = input('inserisci una nuova scelta: ') 
        elif scelta == 'visualizza':
            man.visualizza_menu()
            scelta = input('inserisci una nuova scelta: ')  
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
        x = input('sei il manager o il cliente? m per managere e c per cliente: ')
        if x == 'm':
            print('Fai la tua prima scelta tra modifica aggiungi elimina visualizza e esci')   
            scelta = input()
            menu_manager(scelta)
        elif x == 'c':
            x = cliente
            cliente.crea_profilo()
            print('Fai la tua prima scelta tra ordina conto e esci')   
            scelta = input()
            menu_cliente(scelta)
        else:
            print('Errore')       
    elif entrata_uscita == '0':
        print('Arrivederci')
        flag = False             
    else:
         print('ERRORE')         