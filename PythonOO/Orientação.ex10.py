class Nota_Fiscal:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produtos, icms, frete, ipi):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0
        self.calcular_valor_total()

    def obter_numero(self):
        return self.numero

    def obter_data_emissao(self):
        return self.data

    def alterar_razao_social(self, nova_razao_social):
        self.razao_social = nova_razao_social

    def calcular_valor_total(self):
        self.valor_total = self.valor_produtos + self.icms + self.frete + self.ipi
        return self.valor_total

nf = Nota_Fiscal(
    numero=12345,
    tipo='Saída',
    serie=1,
    cnpj='12.345.678/0001-90',
    razao_social='Empresa X',
    data='2024-07-03',
    valor_produtos=1000.00,
    icms=180.00,
    frete=50.00,
    ipi=70.00
)

print("Número:", nf.obter_numero())
print("Data de Emissão:", nf.obter_data_emissao())
print("Razão Social:", nf.razao_social)
print("Valor Total:", nf.calcular_valor_total())

nf.alterar_razao_social('Nova Empresa Y')
print("Nova Razão Social:", nf.razao_social)