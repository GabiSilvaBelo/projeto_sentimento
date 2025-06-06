import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import re
import os

# Caminho absoluto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "raw", "avaliacoes.csv")
processed_file_path = os.path.join(BASE_DIR, "data", "processed", "avaliacoes_limpo.csv")

df = pd.read_csv(file_path)

def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    stop_words = set(stopwords.words('portuguese'))
    palavras = texto.split()
    palavras = [p for p in palavras if p not in stop_words]
    return ' '.join(palavras)

if __name__ == "__main__":
    # Use o mesmo caminho absoluto aqui!
    df = pd.read_csv(file_path)
    df['texto_limpo'] = df['texto_avaliacao'].apply(limpar_texto)
    df.to_csv(processed_file_path, index=False)
    print("Arquivo salvo em:", processed_file_path)
