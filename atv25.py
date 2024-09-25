# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).
contador = 0
for c in range(5):
    n=int(input("Digite a nota dos alunos:"))

    if n>=7:
        contador+=1

print(f"{contador} alunos estão aprovados")


            
        
