""" Data una ista di numeri togliere i duplicati ma mantenere l'ordine"""

lista = list(input(' inserisci una lista di numeri'))
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