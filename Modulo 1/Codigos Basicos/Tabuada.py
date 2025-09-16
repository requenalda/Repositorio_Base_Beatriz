numero = int(input("Digite um número para fazer a tabuada?"))
numero_inicio = int(input("Digite um número de inicio:"))
numero_fim = int(input("Digite um número para terminar:"))

for i in range(1, 11):
    print(f" {i} x {numero} = {i * numero}")
