pruduto = float(input("digite o valor do produto: "))
if (pruduto <= 50):
    taxa = pruduto + (pruduto * 0.05)
    print(taxa)
elif (pruduto > 50 and pruduto <= 100):
    taxa = pruduto + (pruduto * 0.10)
    print(taxa)
else:
        taxa = pruduto + (pruduto * 0.15)
        print(taxa)

