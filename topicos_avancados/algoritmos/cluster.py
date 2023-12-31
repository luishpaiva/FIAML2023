# -*- coding: utf-8 -*-
"""Cluster.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v7tILTorR2fxfWtUZUk54Xh8ebYaiy8c
"""

from sklearn import datasets
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

from hopkins import *
from metric import *
from visual_assessment_of_tendency import *

import warnings
warnings.filterwarnings("ignore", category = FutureWarning)

iris = datasets.load_iris()
clust1 = scale(iris.data)
clust2 = scale(np.random.rand(150, 4))

print(clust2)

inertia = []

for i in range(1, 8):
  kmeans = KMeans(n_clusters = i, n_init = 'auto')
  kmeans.fit(clust1)
  inertia.append(kmeans.inertia_)

plt.plot(range(1, 8), inertia)
plt.title("Elbow")
plt.show()

inertia = []

for i in range(1, 8):
  kmeans = KMeans(n_clusters = i, n_init = 'auto')
  kmeans.fit(clust2)
  inertia.append(kmeans.inertia_)

plt.plot(range(1, 8), inertia)
plt.title("Elbow")
plt.show()

hopkins(clust1, 150)

hopkins(clust2, 150)

vat(clust1)

vat(clust2)

ivat(clust1)

ivat(clust2)

m = assess_tendency_by_metric(clust1, 'silhouette', 5)
print(m)

m = assess_tendency_by_metric(clust1, 'davies_bouldin', 5)
print(m)

m = assess_tendency_by_metric(clust1, 'calinski_harabasz', 5)
print(m)

m = assess_tendency_by_metric(clust2, 'silhouette', 5)
print(m)

m = assess_tendency_by_metric(clust2, 'davies_bouldin', 5)
print(m)

m = assess_tendency_by_metric(clust2, 'calinski_harabasz', 5)
print(m)

m = assess_tendency_by_mean_metric_score(clust1, 5)
print(m)

m = assess_tendency_by_mean_metric_score(clust2, 5)
print(m)

