# coding: utf-8

import numpy as np
import pretraitement as pt

def createClasses(data):
    membresClasses = np.zeros(10) 
    classes = np.zeros((32,32,10))

    for i in range(0, 73257):
        label = data["y"][i]
        membresClasses[label%10] = membresClasses[label%10] + 1
        imgGray = pt.contrast(data,i)

        for j in range (0,32):
            for k in range (0,32):
                classes[j][k][label%10] = classes[j][k][label%10] + imgGray[j][k]
    
    for i in range(0,32):
        for j in range(0,32):
            for k in range(0,10):
                 classes[i][j][k] = classes[i][j][k]/membresClasses[k]
    
    return classes


def compareWithClasses(testData,indexImg,classe):
    imageGray = pt.contrast(testData,indexImg)
    """
    score = 0
    for i in range(0,32):
        for j in range(0,32):
            score = score + np.abs(classe[i][j] - imageGray[i][j])
    """
    return np.linalg.norm(imageGray - classe)


