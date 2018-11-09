import pretraitement as pt
from scipy.io import loadmat
import matplotlib.pyplot as plt
import class_chiffres as cc
import test_analyze as ta
import pickle

#train_data = loadmat('train_32x32.mat')
test_data = loadmat('test_32x32.mat')

with open ('classes_Chiffres', 'rb') as fp:
    classes = pickle.load(fp)

#with open('classes_Chiffres', 'wb') as fp:
#    pickle.dump(classes, fp)

index = 0

print('Label:', test_data['y'][index])


nbCorrect = 0
for i in range (0,1000):
	if (i%100 == 0):
		print(i)
	calcLabel = ta.bestLabel(classes,test_data,i)
	if (test_data['y'][i] == calcLabel):
		nbCorrect = nbCorrect + 1

print("Pourcentage : ",(nbCorrect/1000) * 100)

#plt.imshow(classes[:,:,2],cmap = 'gray')

plt.imshow(test_data["X"][:,:,:,index],cmap = 'gray')
plt.show()