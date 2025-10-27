import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --- aqui são os valores da matriz de confusão do SVM ---
# Ordem: [[Verdadeiro Negativo, Falso Positivo],
#         [Falso Negativo, Verdadeiro Positivo]]
cm = np.array([[5116, 93],     
               [236, 4974]])

# ---  Nomes das classes (na ordem correta) ---
labels = ['n_cyberbullying', 'cyberbullying']

# --- 3️⃣ Normalização por linha (para ver proporção de acertos e erros por classe) ---
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

# --- 4️⃣ Criação do heatmap ---
plt.figure(figsize=(5, 4))
sns.heatmap(cm_normalized,
            annot=True,          # mostra os números
            fmt=".2%",            # mostra em porcentagem
            cmap="Blues",
            xticklabels=labels,
            yticklabels=labels)

# --- 5️⃣ Títulos e rótulos ---
plt.title("Confusion Matrix – Normalized by Row (SVM)")
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.tight_layout()
plt.show()
plt.savefig('heatmap_normalizado_SVM.png', dpi=300, bbox_inches='tight')
