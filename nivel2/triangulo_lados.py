import modulo_triangulo as tri


caminho = 'nivel2/triangulo_lados.txt'
with open(caminho) as arq:
    linhas = arq.readlines()

lados = []
for linha in linhas:
    partes = linha.strip().split()
    for i in range(len(partes)):
        partes[i] = float(partes[i])
    lado = tri.formar_triangulo(partes[0], partes[1], partes[2])
    if lado:
        lados.append(f'Com {partes[0]}, {partes[1]} e {partes[2]} é possível formar um triângulo!')
    else:
        lados.append(f'Com {partes[0]}, {partes[1]} e {partes[2]} NÃO é possível formar um triângulo...')

with open('triangulo_formar.txt', 'w') as arq:
    for lado in lados:
        arq.write(f'{lado}\n')