from fastapi import FastAPI
import pickle

app = FastAPI()

vectorizer = pickle.load(open("../data/processed/vectorizer.pkl", "rb"))
model = pickle.load(open("../data/processed/model.pkl", "rb"))

@app.get("/")
def read_root():
    return {"mensagem": "API de Sentimento no ar!"}

@app.get("/predict/")
def predict_sentiment(texto: str):
    texto_vec = vectorizer.transform([texto])
    pred = model.predict(texto_vec)[0]
    sentimento = "Positivo" if pred==1 else "Negativo"
    return {"sentimento": sentimento}
