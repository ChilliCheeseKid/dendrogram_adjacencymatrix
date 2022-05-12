import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform
import matplotlib.pyplot as plt
import sys
import plotly.figure_factory as ff

# erstellt das Array und legt variablen fest
n = 50
ranNumber = 7

# befüllt das Array in den Abmessungen n und den zahlen n/10
array_init = np.random.randint(ranNumber, size=(n, n))

# symetrisch machen des Arrays
arraySym = np.maximum(array_init, array_init.transpose())

# die Diagonalen des symetrischen Arrays mit Einsen füllen
arrayFinal = arraySym
np.fill_diagonal(arrayFinal, 0)
arrayFinal = 1.0/arrayFinal
arrayFinal[arrayFinal == np.inf] = 0
arrayFinal = arrayFinal * (ranNumber - 1)
# print(arrayFinal)

# Darstellen des Arrays in einem Dendrogramm
# z = linkage(arrayFinal,
#             method='complete')  # verbinden der Datenpunkte zu clustern mit der ward-Funktion (Alternativ die centroid-Funktion oder median nutzen)
# fig = plt.figure(figsize=(20, 10))
# # eigentliche Dendrogramm einstellugen: truncate bei besonders vielen Daten
# dn = dendrogram(z, truncate_mode='none', get_leaves=True, count_sort='descending', show_leaf_counts=True,
#                 leaf_rotation=90)
# plt.xlabel('Daten bis ' + str(n))
# plt.ylabel('distance (centroid)')
# plt.title("test")
# plt.show()


# fig = ff.create_dendrogram(arrayFinal)
# fig.update_layout(width=800, height=500)
# fig.show()


# mat = np.array([[0.0, 2.0, 0.1], [2.0, 0.0, 2.0], [0.1, 2.0, 0.0]])
dists = squareform(arrayFinal)
linkage_matrix = linkage(dists, "complete")
dendrogram(linkage_matrix)
plt.title("test")
plt.show()