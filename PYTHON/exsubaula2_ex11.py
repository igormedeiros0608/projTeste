def lista():
    lista= [
    "1"  "pera",
    "2" "uva",
    "3" "maça",
    "4" "salada mista",
    ]
    for i in (lista):
        print(i)
lista()

#---------------------------------------------------------

def imprime(lista):
    cont= 0
    while cont < len(lista):
        print(f"{cont+1}, {lista[cont]}")
        cont += 1

listacompra = [ 'mamao', 'pera', 'uva', 'banana', 'kiwi']

imprime(listacompra)