# -*- coding: utf-8 -*-
"""Apriori.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uNKuJYq6NznUKewo652cUiCXPc-XVLu7
"""

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

with open('Transacoes.txt', 'r') as f:
  transactions = [line.strip().split(',') for line in f.readlines()]

transactions

te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_array, columns = te.columns_)
df

frequent_itemsets = apriori(df, min_support = 0.5, use_colnames = True)
frequent_itemsets

rules = association_rules(frequent_itemsets, metric = 'confidence', min_threshold = 0.5)
print(rules)
