class alunos:
    def __init__(self, nome, nota, situacao):
        self.nome = nome
        self.nota = nota
        self.situacao = situacao

aluno = [
    alunos("Thiago", 8.5, "aprovado"),
    alunos("Lucas", 7.0, "aprovado"),
    alunos("Pedro", 5.0, "reprovado"),
    alunos("João", 6.5, "aprovado"),
    alunos("Mariana", 9.0, "aprovado"),
    alunos("Carlos", 4.5, "reprovado"),
    alunos("Julia", 7.5, "aprovado"),
    alunos("Rafael", 5.5, "reprovado"),
    alunos("Ana", 11, "aprovado"),
    alunos("Bruno", 3.5, "reprovado"),
    alunos("Gabriel", 6.0, "aprovado"),
    alunos("Rebeca", 9.5, "aprovado"),
    alunos("Matheus", 4.0, "reprovado"),
    alunos("Larissa", 7.8, "aprovado"),
    alunos("Felipe", 5.8, "reprovado")
]

apro = 0
repro = 0

print('===== APROVADOS =====\n')
for i in aluno:
    if i.nota >= 6 and i.nota <= 10:
        apro += 1
        print(f'Nome: {i.nome} | Nota: {i.nota} | {i.situacao}')
print(f'\nAprovados: {apro}\n')

print('===== REPROVADOS =====\n')
for i in aluno:
    if i.nota < 6:
            repro += 1
            print(f'Nome: {i.nome} | Nota: {i.nota} | {i.situacao}')
print(f'\nReprovados: {repro}')


print('===== NOTAS INVÁLIDAS =====\n')
for i in aluno:
    if i.nota > 10:
        print(f'Nome: {i.nome} | Nota: {i.nota} | Nota inválida')
        print('\nNota inválida (maior que 10)')

