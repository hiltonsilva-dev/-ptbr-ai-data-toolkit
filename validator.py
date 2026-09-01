# Validador de dataset PT-BR - Projeto para portfólio de Data Annotation
import json
from langdetect import detect

ARQUIVO = "sample_data.jsonl"

def carregar_dados(caminho):
    linhas = []
    with open(caminho, 'r', encoding='utf-8') as f:
        for num, linha in enumerate(f, 1):
            linhas.append((num, linha))
    return linhas

def validar():
    print(f"Validando {ARQUIVO}...\n")
    
    vistos = set()
    total = 0
    erros = 0

    print("Relatório de Qualidade:")
    
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
            for num_linha, linha in enumerate(arquivo, 1):
                total += 1
                
                # verifica se o json é valido
                try:
                    dados = json.loads(linha)
                except:
                    print(f" - Linha {num_linha}: JSON quebrado")
                    erros += 1
                    continue

                texto = dados.get("text", "")

                # texto vazio
                if not texto or texto.strip() == "":
                    print(f" - Linha {num_linha}: Texto vazio (falha de Data Collection)")
                    erros += 1
                    continue

                # idioma
                try:
                    idioma = detect(texto)
                    if idioma != 'pt':
                        print(f" - Linha {num_linha}: Idioma detectado como '{idioma}'")
                        erros += 1
                except:
                    print(f" - Linha {num_linha}: Erro ao detectar idioma")
                    erros += 1

                # duplicado
                if texto in vistos:
                    print(f" - Linha {num_linha}: Texto duplicado")
                    erros += 1
                else:
                    vistos.add(texto)

    except FileNotFoundError:
        print("Arquivo não encontrado. Verifica se o sample_data.jsonl ta na mesma pasta.")
        return

    print(f"\nTotal de linhas analisadas: {total}")
    print(f"Total de erros encontrados: {erros}")
    
    if total > 0:
        qualidade = ((total - erros) / total) * 100
        print(f"Qualidade do dataset: {qualidade:.0f}%")

if __name__ == "__main__":
    validar()
