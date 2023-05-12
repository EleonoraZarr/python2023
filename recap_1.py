"""data una stringa creae un dizionario con chiavi le lettere della stringa 
e come valori il numero di volte che la lettera appare nella stringa"""

dizionario = {}          #creo un dizionario vuoto

print('Inserire una stringa:  ')
parola = input(' ')

for lettera in parola:                      #scorro le lettere della parola
    if lettera not in dizionario:          # se la lettera non è nel dizionario
        dizionario[lettera]=1              # la aggiungo con valore 1
    else:
        dizionario[lettera] += 1             # altrimenti aumento il valore

print(dizionario)                             # stampo il dizionario

"""for chiave,valore in dizionario.items():            stampa chiave e valore e non il dizionario
  print(chiave, valore) """