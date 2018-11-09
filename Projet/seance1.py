# coding: utf-8

import numpy as np
from scipy.io import loadmat
train_data = loadmat("train_32x32.mat")
test_data = loadmat("test_32x32.mat")

import matplotlib.pyplot as plt

import pickle

def scoreImage(image,modele):
    total = 0
    for i in range (0,32):
        for j in range (0,32):
            total = total + abs( np.average(image[i,j,:]) - modele[i][j] )*abs( np.average(image[i,j,:]) - modele[i][j] )
    return total


lire = True

if (lire):  
    with open ('DataNumbersfile', 'rb') as fp:
        tab7 = pickle.load(fp)
else:
    tab7 = np.zeros((32,32,11))
    nbElem = np.zeros(11)
    
    for i in range (0,73257):
        label = train_data["y"][i]
        print(i)
        nbElem[label] = nbElem[label] + 1
        for j in range (0,32):
            for k in range (0,32):
                tab7[j][k][label] = tab7[j][k][label] + np.average(train_data["X"][j, k, :,i])
 
    for i in range (0,32):
        for j in range (0,32):
            for k in range (0,11):
                tab7[i][j][k] = tab7[i][j][k]/nbElem[k]

    with open('DataNumbersfile', 'wb') as fp:
        pickle.dump(tab7, fp)

"""plt.imshow(tab7[:,:,7])"""
print('Label:', train_data['y'][0])
plt.imshow(train_data['X'][:, :, :, 0])
plt.show()


for i in range (0,11):

    print('Label ',i,' :',scoreImage(train_data['X'][:, :, :, 0],tab7[:,:,i]))


