ptbr-ai-data-toolkit
Toolkit para validação de qualidade de datasets em português do Brasil focado em AI Training e Data Annotation.

Este projeto foi desenvolvido como portfólio para demonstrar habilidades em validação de dados, controle de qualidade e processamento de linguagem natural em PT-BR.

Objetivo
Validar datasets no formato JSONL garantindo:

Detecção de idioma (PT-BR)
Identificação de textos vazios
Deduplicação de entradas
Validação de formato JSON
Estrutura do projeto
ptbr-ai-data-toolkit/
├── validator.py # Script principal de validação
├── sample_data.jsonl # Dataset de exemplo para testes
├── requirements.txt # Dependências
└── README.md

Tecnologias
Python 3.8+
pandas
langdetect
Como usar
Instale as dependências:
pip install -r requirements.txt
Execute o validador:
python validator.py
O script irá analisar o sample_data.jsonl e gerar um relatório de qualidade.

Exemplo de saída
Validando sample_data.jsonl...

Relatório de Qualidade:

Linha 3: Texto vazio (falha de Data Collection)
Linha 4: Idioma detectado como 'en'
Encontrados 1 textos duplicados
Total de linhas analisadas: 5

Caso de uso
Este validador simula o fluxo de trabalho real de um Data Annotator / Content Evaluator, garantindo que apenas dados limpos e em PT-BR nativo cheguem para o treinamento de modelos de IA.

Autor
Hilton Silva - PT-BR Native | Interesse em AI Training e Data Annotation
