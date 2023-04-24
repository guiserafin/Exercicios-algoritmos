notas = {}
freq_base = 16.35 # frequência da nota C0

# preenchendo o dicionário com as frequências de todas as notas
for oitava in range(9):
    for nota in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
        nome = f"{nota}{oitava}"
        freq = freq_base * (2 ** (oitava + (['C', 'D', 'E', 'F', 'G', 'A', 'B'].index(nota) / 12)))
        notas[nome] = freq

nota = input("Digite o nome da nota: ").upper()

if nota in notas:
    print(f"A frequência correspondente a {nota} é {notas[nota]:.2f} Hz")
else:
    print("Nota inválida.")