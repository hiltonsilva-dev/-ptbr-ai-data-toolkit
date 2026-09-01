import json
from langdetect import detect
from collections import Counter

def validate_ptbr_dataset(file_path="sample_data.jsonl"):
    """
    Validador PT-BR para datasets de AI Training
    Criado por Hilton Silva - Portfólio OneForma
    """
    print(f"🔍 Validando {file_path}...\n")
    texts = []
    issues = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            try:
                data = json.loads(line)
                text = data.get("text", "")
                texts.append(text)

                if not text.strip():
                    issues.append(f"Linha {i}: Texto vazio (falha de Data Collection)")
                    continue
                
                try:
                    lang = detect(text)
                    if lang != 'pt':
                        issues.append(f"Linha {i}: Idioma detectado como '{lang}' -> '{text[:40]}...'")
                except:
                    pass
            except json.JSONDecodeError:
                issues.append(f"Linha {i}: JSON inválido (falha de formatação)")

    # Verifica duplicados
    counter = Counter(texts)
    dups = [t for t, c in counter.items() if c > 1 and t.strip()]
    if dups:
        issues.append(f"Encontrados {len(dups)} textos duplicados (falha de deduplicação)")

    if not issues:
        print("✅ Dataset PT-BR 100% limpo e pronto para AI Training!")
    else:
        print("⚠️ Relatório de Qualidade:")
        for issue in issues:
            print(f" - {issue}")
    
    print(f"\n📊 Total de linhas analisadas: {len(texts)}")

if __name__ == "__main__":
    validate_ptbr_dataset()
