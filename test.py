import numpy as np
import sys
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt


#erstellt das Array und legt variablen fest
n= 50
ranNumber = 7

# befüllt das Array in den Abmessungen n und den zahlen n/10
array_init = np.random.randint(ranNumber, size=(n,n))

#symetrisch machen des Arrays
arraySym=np.maximum(array_init,array_init.transpose())

#die Diagonalen des symetrischen Arrays mit Nullen füllen
arrayFinal= arraySym
np.fill_diagonal(arrayFinal, 0)

#print(arrayFinal)

##Darstellen des Arrays in einem Dendrogramm

z = linkage(arrayFinal, method='centroid')  ##verbinden der Datenpunkte zu clustern mit der ward-Funktion (Alternativ die centroid-Funktion oder median nutzen)
fig = plt.figure(figsize=(20, 10))
#eigentliche Dendrogramm einstellugen: truncate bei besonders vielen Daten
dn = dendrogram(z, truncate_mode='none', get_leaves=True, count_sort='descending', show_leaf_counts=True, leaf_rotation=90)
plt.xlabel('Daten bis ' + str(n))
plt.ylabel('distance (centroid)')
plt.title("test")
plt.show()