# === Figura: Dispersão das classes (após balanceamento e contrafactuais) ===
# Reprodutível e com rótulos/infos solicitadas pelo revisor

# encoding: iso-8859-1
import pandas as pd
import funcoes as fun
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import numpy as np

# ---- 1) Carregar e preparar ----

df =  fun.carregarCSV('./dataset_inicial.csv')
#df =  fun.carregarCSV('./dataset_intermediario.csv')
#df = fun.carregarCSV('./dataset.csv')
df.columns = df.columns.str.strip()
df['Classific'] = df['Classific'].astype(str).str.strip().str.lower()
df['Texto'] = df['Texto'].astype(str)

# Mapear classes p/ máscara
y = df['Classific'].map({'cyberbullying': 1, 'n_cyberbullying': 0}).values

# Contagens por classe e total
n_pos = int((df['Classific'] == 'cyberbullying').sum())
n_neg = int((df['Classific'] == 'n_cyberbullying').sum())
N = n_pos + n_neg

# ---- 2) TF-IDF (1–2 grams) ----
vectorizer = TfidfVectorizer(
    max_features=5000,       # configuração original de dimensão
    ngram_range=(1, 2),      # explícito no rótulo
    lowercase=True
)
X_tfidf = vectorizer.fit_transform(df['Texto'])
vocab_size = len(vectorizer.vocabulary_)  # dimensão efetiva (<= max_features)

# ---- 3) Redução p/ 2D com TruncatedSVD (PCA p/ esparsos) ----
svd = TruncatedSVD(n_components=2, random_state=42)
X_2d = svd.fit_transform(X_tfidf)
var1, var2 = svd.explained_variance_ratio_[0]*100, svd.explained_variance_ratio_[1]*100

# ---- 4) Plot com rótulos informativos ----
mask_neg = (y == 0)
mask_pos = (y == 1)

plt.figure(figsize=(8, 6), dpi=120)
plt.scatter(X_2d[mask_neg, 0], X_2d[mask_neg, 1], s=10, alpha=0.5, label='n_cyberbullying')
plt.scatter(X_2d[mask_pos, 0], X_2d[mask_pos, 1], s=10, alpha=0.5, label='cyberbullying')

plt.xlabel(f'Component 1 (TruncatedSVD) – {var1:.2f}% variance explained')
plt.ylabel(f'Component 2 (TruncatedSVD) – {var2:.2f}% variance explained')

plt.title(
    'Dispersion of classes before balancing \n'
    f'TF-IDF (1–2 grams), vocab size={vocab_size}, N={N}'
)

plt.legend(title=f'Counts  |  n_cyberbullying={n_neg}  •  cyberbullying={n_pos}')
plt.grid(True, linewidth=0.4, alpha=0.6)
plt.tight_layout()
plt.savefig('figure_dispersion_inicial_new2.png', dpi=300, bbox_inches='tight')
# plt.show()
