"""Número de matrícula. Suponha que uma escola utilize, como código de matrícula, um
número inteiro no formato AASDDD, onde:
• os dois primeiros dígitos, representados pela letra A, são os dois últimos algarismos do ano
da matrícula;
• o terceiro dígitos, representado pela letra S, vale 1 ou 2, conforme o aluno tenha se
matriculado no 1o ou 2o semestre;
• os três últimos dígitos, representados pela letra D, correspondem à ordem da matrícula do
aluno, no semestre e no ano em questão.
Crie um programa Python que leia o número de matrícula de um aluno e imprima o ano e o
semestre em que ele foi matriculado. Por exemplo, um número de matrícula 182034 deve
resultar ano 18 e semestre 2."""

numeroMatricula = int(input("Insira o número da matrícula do aluno: "))

numeroMatricula = str(numeroMatricula)
ano = numeroMatricula[0] + numeroMatricula[1]

semestre = numeroMatricula[2]

print(f"O ano da matrícula é {ano} e o semstre é o {semestre}o")