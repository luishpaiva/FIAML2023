# -*- coding: utf-8 -*-
"""SelecaoAtributos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HlwqzDbyPemewMCsewRwD_sOynRst3Vu
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import chi2, SelectKBest

from google.colab import files
uploaded = files.upload()

anuncio = pd.read_csv('ad.data', header = None)
anuncio.shape

X = anuncio.iloc[:,:-1].values
y = anuncio.iloc[:,-1].values

X

y

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y, test_size = 0.3, random_state = 0)

modelo1 = GaussianNB()
modelo1.fit(X_treinamento, y_treinamento)
previsoes1 = modelo1.predict(X_teste)
print(accuracy_score(y_teste, previsoes1))

selecao = SelectKBest(chi2, k = 7)
X_novo = selecao.fit_transform(X, y)

X_novo

X_novo.shape

print(selecao.get_support())

X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X_novo, y, test_size = 0.3, random_state = 0)

modelo2 = GaussianNB()
modelo2.fit(X_treinamento, y_treinamento)
previsoes2 = modelo2.predict(X_teste)
print(accuracy_score(y_teste, previsoes2))

