# encoding: iso-8859-1
import pprint
from sklearn import svm
from sklearn import datasets
import pandas as pd
import joblib
from joblib import dump, load
from sklearn.feature_extraction.text import TfidfVectorizer
import pprint 
import emoji
import re
import funcoes as fun 
import pickle
import csv


# Função para separar emojis do texto
def separar_emojis(texto):
    texto = emoji.replace_emoji(texto, replace=lambda e, data: f' {e} ')
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

# Tokenizador que reconhece emojis como tokens separados
def tokenizer_emoji_aware(text):
    text = separar_emojis(text)
    return text.split()


def classificar_frase_svm(modelo,vectorizer,frase):
    frase_vec = vectorizer.transform([frase])
    pred = modelo.predict(frase_vec)[0]
    if pred == "cyberbullying" or pred == 1:
        return "Segundo o modelo treinado com SVM, a frase informada tem potencial de ser cyberbullying.", True
    else:
        return " Segundo o modelo treinado com SVM, a frase informada aparentemente não é considerada cyberbullying.", False


def classificar_frase_nb(modelo_nb,vectorizer_nb,frase):
    frase_vec = vectorizer_nb.transform([frase])
    pred = modelo_nb.predict(frase_vec)[0]
    if pred == "cyberbullying" or pred == 1:
        return "Segundo o modelo treinado com Naive Bayes, a frase informada tem potencial de ser cyberbullying.",True
    else:
        return "Segundo o modelo treinado com Naive Bayes, a frase informada aparentemente não é considerada cyberbullying.",False


# open("bully_binary_classification\\"+data_set+"\\features\\selected\\X_Toxicity.pkl",'wb') as f:
#     pickle.dump(X_Toxicity, f)

def salvarmodelob(modelo,filename):
    with open(filename,'wb') as f:
        pickle.dump(modelo, f)

# def  carregarmodelob(filename):
#     with open(filename, 'rb') as fo:
#         joblib.load(fo)
    
#     return load(filename)


# save
def salvarmodelo(modelo,filename):
    dump(modelo, filename)


def  carregarmodelo(filename):
    return load(filename)



def carregarCSV(arquivo):
 return pd.read_csv(arquivo,encoding='utf-8')


def salvar(nome_ark,arquivo):
    f = open(nome_ark, "a+")
    f.write(str(arquivo)+"\r\n")
    f.close()


def ler(arquivo):
    return  open(arquivo, 'r')



