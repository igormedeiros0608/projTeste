def somaImposto(taxaImposto, custo):
    imposto = custo + (custo * (taxaImposto / 100))
    return imposto

taxa = float(input("Por favor, insira a taxa de imposto (em %): "))
custo = float(input("Por favor, insira o custo do item: "))
valorfim = somaImposto(taxa, custo)
print(f"O valor do item com imposto é: {valorfim}")