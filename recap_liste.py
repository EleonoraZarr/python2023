""" Data una ista di numeri togliere i duplicati ma mantenere l'ordine

lista = list(input(' inserisci una lista di numeri'))       # questo codice funziona solo per i numeri da 0 a 9
print('Hai inserito: ',lista)

for el in lista:
    if el==' ':
        lista.remove(el)
print('La lista senza spazi è: ',lista)        

lista_senza_doppi = []
for el in lista:
    if el not in lista_senza_doppi:
        lista_senza_doppi.append(el)
print('La lista senza doppi è: ',lista_senza_doppi)
"""

# questo funziona con tutti i numeri
stringa = input(' inserisci una lista di numeri separati da , ')      
print('Hai inserito: ',stringa)
stringa = stringa.replace(' ','').split(',')
       

lista_senza_doppi = []
for el in stringa:
    if el not in lista_senza_doppi:
        lista_senza_doppi.append(el)
print('La lista senza doppi è: ',lista_senza_doppi)