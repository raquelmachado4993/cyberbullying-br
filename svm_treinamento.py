# encoding: iso-8859-1
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
import pandas as pd
import emoji
import re
import pprint
from datetime import datetime
import pprint
import joblib
import  funcoes as fun 



# Fun��o para separar emojis do texto
def separar_emojis(texto):
    texto = emoji.replace_emoji(texto, replace=lambda e, data: f' {e} ')
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

# Tokenizador que reconhece emojis como tokens separados
def tokenizer_emoji_aware(text):
    text = separar_emojis(text)
    return text.split()

# l� o  arquivo do dataset, � um csv
df =  fun.carregarCSV('./dataset.csv')

print(datetime.now()) #talvez precise mostrar o tempo que demorou pra treinar?

df.columns = df.columns.str.strip()
# Pr�-processamento do texto no DataFrame - usando apenas as colunas importantes do csv
df['Texto'] = df['Texto'].apply(separar_emojis)

X = df['Texto']
y = df['Classific']


# Divis�o dos dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Vetoriza��o com TF-IDF e tokeniza��o sens�vel a emojis
vectorizer = TfidfVectorizer(
    tokenizer=tokenizer_emoji_aware,
    ngram_range=(1, 2),
    lowercase=True
)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# salva o vetor
filenamev = 'finalized_svm_vectorizer.joblib'
fun.salvarmodelo(vectorizer,filenamev)


# Treinamento do modelo SVM
model = SVC(kernel='linear', C=10.0, random_state=42)
model.fit(X_train_vec, y_train)

# salvando o modelo
filename = 'finalized_svm_model.joblib'
fun.salvarmodelo(model,filename)

# Avalia��o do modelo
y_pred = model.predict(X_test_vec)

print("\nRelat�rio de Classifica��o:")
print(classification_report(y_test, y_pred, digits=4))

# Matriz de confus�o e c�lculo dos valores VP, VN, FP, FN
cm = confusion_matrix(y_test, y_pred, labels=['n_cyberbullying', 'cyberbullying'])
print("\nMatriz de Confus�o:")
print(cm)

VN, FP, FN, VP = cm.ravel()

print(f"Verdadeiro Negativo (VN): {VN}")
print(f"Falso Positivo (FP): {FP}")
print(f"Falso Negativo (FN): {FN}")
print(f"Verdadeiro Positivo (VP): {VP}")

# C�lculo das m�tricas
pos_label = 'cyberbullying' if 'cyberbullying' in y_test.values else 1

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label=pos_label)
recall = recall_score(y_test, y_pred, pos_label=pos_label)
f1 = f1_score(y_test, y_pred, pos_label=pos_label)

#salvando isso
fun.salvar("rel_class_svn.txt","Acuracia: "+str(accuracy)+", Precisao: "+str(precision)+", Recall: "+str(recall)+", F1-Score: "+str(f1)+"")

print(f"\nAcur�cia: {accuracy:.4f}")
print(f"Precis�o: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

print(datetime.now())
