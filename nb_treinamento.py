# encoding: iso-8859-1
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import emoji
import re
import pandas as pd
import funcoes as fun
import joblib
from joblib import dump, load
import pprint


# Função para separar emojis como tokens individuais
def separar_emojis(texto):
    texto = emoji.replace_emoji(texto, replace=lambda e, data: f' {e} ')
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

# Tokenizador que reconhece emojis como tokens separados
def tokenizer_emoji_aware(text):
    text = separar_emojis(text)
    return text.split()


# lê o  arquivo do dataset, é um csv
df =  fun.carregarCSV('./dataset.csv')

# Aplica separação de emojis ao texto
df['Texto'] = df['Texto'].apply(separar_emojis)

# Divide em variáveis de entrada (X) e rótulo (y)
X = df['Texto']
y = df['Classific']

# Separa os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Vetorização com TF-IDF e separação de emojis
vectorizer_nb = TfidfVectorizer(tokenizer=tokenizer_emoji_aware, ngram_range=(1, 2),lowercase=True)


X_train_vec = vectorizer_nb.fit_transform(X_train)
X_test_vec = vectorizer_nb.transform(X_test)

# salvando o vector 
fun.salvarmodelo(vectorizer_nb,'finalized_nb_vectorizer.joblib')

# Treinamento com Naive Bayes
modelo_nb = MultinomialNB()
modelo_nb.fit(X_train_vec, y_train)

# salvando o modelo
filename = 'finalized_nb_model.joblib'
fun.salvarmodelo(modelo_nb,filename)

# Predição
y_pred_nb = modelo_nb.predict(X_test_vec)

# Avaliação
print("\n Relatório de Classificação (Naive Bayes):")
print(classification_report(y_test, y_pred_nb, digits=4))

print("\n Matriz de Confusão:")
print(confusion_matrix(y_test, y_pred_nb))

# Cálculo manual das métricas (com base na sua tese)
pos_label = 'cyberbullying' if 'cyberbullying' in y_test.values else 1
accuracy = accuracy_score(y_test, y_pred_nb)
precision = precision_score(y_test, y_pred_nb, pos_label=pos_label)
recall = recall_score(y_test, y_pred_nb, pos_label=pos_label)
f1 = f1_score(y_test, y_pred_nb, pos_label=pos_label)

print(f"\n Acurácia: {accuracy:.4f}")
print(f" Precisão: {precision:.4f}")
print(f" Recall: {recall:.4f}")
print(f" F1-Score: {f1:.4f}")