"""data una stringa creae un dizionario con chiavi le lettere della stringa 
e come valori il numero di volte che la lettera appare nella stringa"""

dizionario = {}

print('Inserire una stringa:  ')
parola = input(' ')

for lettera in parola:
    if lettera not in dizionario:  
        dizionario[lettera]=1
    else:
        dizionario[lettera] += 1 

print(dizionario)

"""for chiave,valore in dizionario.items():   
  print(chiave, valore) """