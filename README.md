# Projeto Sentimento

Este projeto é um pipeline completo de Ciência de Dados para análise de sentimentos em avaliações de texto, utilizando técnicas de Processamento de Linguagem Natural (PLN), Machine Learning, deploy via API e uso de Docker.

---

## 📚 Conteúdo do projeto

- Pré-processamento de dados com Python e NLTK
- Treinamento e avaliação de modelos de aprendizado de máquina
- API REST para servir o modelo usando FastAPI e Uvicorn
- Containerização com Docker
- Uso de banco de dados SQL para armazenar dados processados
- Integração com Git e controle de versão

---

## 🚀 Como rodar o projeto localmente

### Pré-requisitos

- Python 3.8+
- Docker (opcional, para rodar com container)
- Git

### Passos para rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto_sentimento.git
   cd projeto_sentimento


python3 -m venv .venv
source .venv/bin/activate  # no Linux/Mac
.\.venv\Scripts\activate   # no Windows


pip install -r requirements.txt


python src/data_preprocessing.py


uvicorn src.deploy_api:app --reload


projeto_sentimento/
├── data/                   # Dados brutos e processados
├── src/                    # Código fonte (preprocessamento, API, modelagem)
├── .gitignore              # Arquivos e pastas ignoradas pelo Git
├── Dockerfile              # Arquivo para containerizar o projeto
├── requirements.txt        # Dependências do Python
└── README.md               # Este arquivo

🛠 Tecnologias utilizadas

Python 3.8+
Pandas, Numpy, Scikit-learn
NLTK (Processamento de Linguagem Natural)
FastAPI, Uvicorn (API REST)
Docker
Git e GitHub
SQLite (ou outro banco SQL)
Big Data (conceitos aplicados no projeto)
