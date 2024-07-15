lista = []
print("Introduza as notas (entre 0 e 10). Para terminar, introduza um valor fora deste intervalo.")
while True:
    entrada = input("Digite uma nota: ")
    nota = float(entrada)
    if 0 <= nota <= 10:
            lista.append(nota)
    else:
            break


res = sum(lista) / len(lista)
print(f"A media das notas é {res}")