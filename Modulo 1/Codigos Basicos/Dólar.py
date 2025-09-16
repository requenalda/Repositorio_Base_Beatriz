def Dólar_para_real(Dólar):
    cotação = 5.30 #exemplo de cotação
    return Dólar * cotação
def real_para_Dólar(real):
    cotação = 5.30 #exemplo de cotação
    return real / cotação
#menu interativo
print("Conversor de Moedas")
print("[1] - Converter Dólar para real")
print("[2] - Converter real para Dólar")
opção = int(input("Escolha a opção:"))
if opção == 1:
    valor = float(input("Digite o valor em Dólar: $"))

    Dólar_para_real(valor)
print = float(input("Digite o valor em real: $"))
