""" scrivo in input una frase, ceare un dizionario che conta le parole in una frase """

frase = input('inserisci una frase: ')

lista = frase.split(' ')
print(lista)

dizionario = {} 

for parola in lista:                      #scorro le lettere della parola
    if parola not in dizionario:          # se la lettera non è nel dizionario
        dizionario[parola]=1              # la aggiungo con valore 1
    else:
        dizionario[parola] += 1             # altrimenti aumento il valore

print(dizionario)