# ptbr-ai-data-toolkit

Meu toolkit simples pra validar dados em português do Brasil.

Fiz pra meu portfólio OneForma - parte de Data QA / Annotation.

## O que faz

Esse script valida um arquivo jsonl e ve se tem erro comum:
- texto vazio
- json quebrado
- espaço duplo
- texto duplicado no mesmo lote

Nada de lib complicada, só python puro mesmo.

## Como usei aqui em Caetité

1. coloquei meus dados no sample_data.jsonl
2. rodei python validator.py
3. vi o relatório no terminal

Exemplo:
python validator.py

Saida:
Validando sample_data.jsonl...
Total: 6 / Validos: 6 / Erros: 0
Qualidade: 100.0%

## Arquivos

- validator.py - meu validador principal
- sample_data.jsonl - meu lote de exemplo com 6 frases em pt-br que eu criei
- requirements.txt - sem nada externo, só python

Feito em ago/2025 no meu notebook, Python 3.10.
Hilton Silva - Caetité BA
