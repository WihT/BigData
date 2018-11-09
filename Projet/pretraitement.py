# coding: utf-8

import numpy as np
from scipy.io import loadmat

def averageLightness(train_data,indexOfImg):
	grayImg = np.zeros((32,32))
	for i in range (0,32):
		for j in range (0,32):
			maxi = max(train_data["X"][i,j,0,indexOfImg],train_data["X"][i,j,1,indexOfImg],train_data["X"][i,j,2,indexOfImg])
			mini = min(train_data["X"][i,j,0,indexOfImg],train_data["X"][i,j,1,indexOfImg],train_data["X"][i,j,2,indexOfImg])
			grayImg[i][j] = (maxi + mini)/2
	return grayImg

def average(train_data,indexOfImg):
	grayImg = np.zeros((32,32))
	for i in range (0,32):
		for j in range (0,32):
			grayImg[i][j] = np.average(train_data["X"][i,j,:,indexOfImg])
	return grayImg

def averageLuminosity(train_data,indexOfImg):
	grayImg = np.zeros((32,32))
	for i in range (0,32):
		for j in range (0,32):
			grayImg[i][j] = 0.21 * train_data["X"][i,j,0,indexOfImg] + 0.72 * train_data["X"][i,j,1,indexOfImg] + 0.07 * train_data["X"][i,j,2,indexOfImg]
	return grayImg

def contrast(train_data,indexOfImg):
	moyenne = 0
	grayImg = np.zeros((32,32))
	tmpImg = np.zeros((32,32))
	for i in range (0,32):
		for j in range (0,32):
			tmpImg[i][j] = 0.21 * train_data["X"][i,j,0,indexOfImg] + 0.72 * train_data["X"][i,j,1,indexOfImg] + 0.07 * train_data["X"][i,j,2,indexOfImg]
			moyenne = moyenne + tmpImg[i][j]

	moyenne = moyenne/1024

	for i in range (0,32):
		for j in range (0,32):
			grayImg[i][j] = (tmpImg[i][j] * (tmpImg[i][j]/moyenne))%255
			#grayImg[i][j] = (2 * tmpImg[i][j] - moyenne)%255
	return grayImg

def tryHard(train_data,indexOfImg):
	return 0

