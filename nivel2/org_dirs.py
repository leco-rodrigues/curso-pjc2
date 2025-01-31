import os


# Programa que organiza arquivos em pastas dependendo da extensão

# Passo 1: Processar (ler) a pasta a ser organizada
ORG_DIR = 'C:/Users/Usuario/Documents/Org_Dirs'
ARQUIVOS = f'{ORG_DIR}/Arquivos'

# Passo 2: Criar sub-pastas para cada tipo de arquivo (fotos, videos, audios, texto etc)
FOTOS = f'{ORG_DIR}/Fotos'
VIDEOS = f'{ORG_DIR}/Videos'
AUDIOS = f'{ORG_DIR}/Audios'
TEXTO = f'{ORG_DIR}/Textos'
if not os.path.exists(FOTOS):
    os.makedirs(FOTOS)
if not os.path.exists(VIDEOS):
    os.makedirs(VIDEOS)
if not os.path.exists(AUDIOS):
    os.makedirs(AUDIOS)
if not os.path.exists(TEXTO):
    os.makedirs(TEXTO)

# Passo 3: Filtrar e mover cada arquivo para sua devida pasta
for arq in os.listdir(ARQUIVOS):
    if arq.endswith('.jpg'):
        os.rename(f'{ARQUIVOS}/' + f'{arq}', f'{FOTOS}/' + f'{arq}')
    if arq.endswith('.mp4'):
        os.rename(f'{ARQUIVOS}/' + f'{arq}', f'{VIDEOS}/' + f'{arq}')
    if arq.endswith('.mp3'):
        os.rename(f'{ARQUIVOS}/' + f'{arq}', f'{AUDIOS}/' + f'{arq}')
    if arq.endswith(('.pdf', '.csv', '.ipynb', '.arq', '.py')):
        os.rename(f'{ARQUIVOS}/' + f'{arq}', f'{TEXTO}/' + f'{arq}')
# ------------------------------------------------------------------ [Exercício] Aula 13