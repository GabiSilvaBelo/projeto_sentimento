import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

df = pd.read_csv("data/processed/avaliacoes_limpo.csv")

X = df['texto_limpo']
y = df['nota'].apply(lambda x: 1 if x >=4 else 0)  # 1=positivo, 0=negativo

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

with open("../data/processed/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("../data/processed/model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Modelo treinado e salvo com sucesso!")