nome = input("Qual é seu nome? ")
peso = float(input("Qual é seu peso? "))
altura = float(input("Qual é sua altura? "))
IMC = peso/(altura*altura)
if imc>=18.5:
    print("abaixo do peso")
elif imc>=24.9:
    print("peso normal")
elif imc>=29.9:
    print(f" {nome} esta com Obesidade Grau I {imc}")
elif imc>=39.9:
    print(f" {nome} esta com Obesidade Grau II {imc}")
else:
    print(f" {nome} esta com Obesidade Grau III (mórbida) {imc}")
