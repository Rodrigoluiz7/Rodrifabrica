notas = []
for i in range(5):
    nota = float(input(f'Digite a nota do aluno {i+1}: '))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f'A média dos alunos é: {media}')
