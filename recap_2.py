""" scrivo in input una frase, ceare un dizionario che conta le parole in una frase """

frase = input('inserisci una frase: ')

simboli = [',',';','.',':','?','!']
for lett in frase:
    if lett in simboli:
        frase = frase.replace(lett,'')      #cancello i simboli

lista = frase.split(' ')                    # trasformo la stringa in una lista


dizionario = {} 

for parola in lista:                      #scorro le parole della frase
    if parola not in dizionario:          # se la parola non è nel dizionario
        dizionario[parola]=1              # la aggiungo con valore 1
    else:
        dizionario[parola] += 1             # altrimenti aumento il valore

print(dizionario)