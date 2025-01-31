import nivel2.triangulo_utils as tri


# Passo 1: Processar (ler) o arquivo "tri_vertice.txt"
caminho = "nivel2/triangulo_vertices.txt"
with open(caminho) as arq:
    conteudo = arq.readlines()
    lados = []

# Passo 2: Calcular cada lado do possível triângulo
for linha in conteudo:
    partes = linha.strip().split()
    for i in range(len(partes)):
        partes[i] = float(partes[i])
    resposta = tri.comprimento_triangulo(partes[0], partes[1], partes[2], partes[3])
    lados.append(resposta)

# Passo 3: Processar (escrever) o arquivo "tri_lados,txt"
caminho_2 = "nivel2/triangulo_lados.txt"
with open(caminho_2, "w") as arq:
    for resp in lados:
        arq.writelines(f'{resp}\n')

# Passo 4: Processar (ler) o arquivo "triangulo_lados.txt"
with open(caminho_2) as arq:
    conteudo = arq.readlines()
    triangulo = []
    perimetro = []
    area = []

# Passo 5: Verificar se é possível criar um triângulo
for linha_2 in conteudo:
    linha_2 = linha_2.strip()
    linha_2 = linha_2.replace('(', '').replace(')', '').replace(',', '')
    linha_2 = linha_2.split()
    for i in range(len(linha_2)):
        linha_2[i] = float(linha_2[i])
    resposta_2 = tri.formar_triangulo(linha_2[0], linha_2[1], linha_2[2])
    if resposta_2:
        triangulo.append(resposta_2)

# Passo 6: Calcular o Perímetro e a Área dos triângulos
        perimetro_tri = tri.perimetro_triangulo(linha_2[0], linha_2[1], linha_2[2]) # Perímetro
        perimetro.append(perimetro_tri)
        area_tri = tri.area_triangulo(linha_2[0], linha_2[1], linha_2[2]) # Área
        area.append(area_tri)
    else:
        triangulo.append("Acho que não...")

# Passo 7: Processar (escrever) os arquivos "triangulo_verdadeiro.txt", "triangulo_perimetro.txt", "triangulo_area.txt"
caminho_3 = "nivel2/triangulo_verdadeiro.txt"
with open(caminho_3, 'w') as arq:
    for resp in triangulo:
        arq.writelines(f'{resp}\n')

caminho_4 = "nivel2/triangulo_perimetro.txt"
with open(caminho_4, 'w') as arq:
    for resp in perimetro:
        arq.writelines(f'{resp}\n')

caminho_5 = "nivel2/triangulo_area.txt"
with open(caminho_5, 'w') as arq:
    for resp in area:
        arq.writelines(f'{resp}\n')
# --------------------------------- [Exercício] Aula 12