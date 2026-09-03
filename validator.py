# ptbr-ai-data-toolkit - validador de dados PT-BR
# feito por Hilton - Caetité/BA pra portfólio OneForma
# pra validar dados de treinamento de IA e anotação
# criei em agosto/25, uso simples sem frescura
# roda só com python padrão, sem langdetect nem nada externo

import json
from pathlib import Path

ARQUIVO = "sample_data.jsonl"

def carregar_dados(caminho):
    # carrego aqui meu lote, linha por linha
    linhas = []
    p = Path(caminho)
    if not p.exists():
        print(f"nao achei arquivo: {caminho}")
        return []
    
    with open(p, 'r', encoding='utf-8') as f:
        for num, linha in enumerate(f, 1):
            linhas.append((num, linha.strip()))
    return linhas

def validar():
    print(f"Validando {ARQUIVO}...\n")
    
    vistos = set()
    total = 0
    erros = 0
    ok = 0

    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as arquiv:
            for num_linha, linha in enumerate(arquiv, 1):
                total += 1
                
                if not linha.strip():
                    print(f" - Linha {num_linha}: vazia, pulei")
                    erros += 1
                    continue

                # ve se json ta ok
                try:
                    dados = json.loads(linha)
                except:
                    print(f" - Linha {num_linha}: JSON invalido")
                    erros += 1
                    continue

                texto = dados.get("text", "")

                # texto vazio
                if not texto or texto.strip() == "":
                    print(f" - Linha {num_linha}: Texto vazio")
                    erros += 1
                    continue

                # espaco duplo - meu check basico
                if "  " in texto:
                    print(f" - Linha {num_linha}: espaco duplo")
                    erros += 1
                    continue

                # duplicado
                if texto in vistos:
                    print(f" - Linha {num_linha}: duplicado")
                    erros += 1
                    continue
                else:
                    vistos.add(texto)
                    ok += 1

    except FileNotFoundError:
        print(f"arquivo {ARQUIVO} nao encontrado na pasta")
        return

    print("\nRelatorio de Qualidade:")
    print(f"Total: {total} / Validos: {ok} / Erros: {erros}")
    if total > 0:
        qual = (ok/total)*100
        print(f"Qualidade: {qual:.1f}%")

if __name__ == "__main__":
    validar()
