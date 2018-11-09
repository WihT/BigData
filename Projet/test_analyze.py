import class_chiffres as cc

def bestLabel(classes,test_data,indexImg):#Marche mal 11,4 %
	
	for i in range(0,10):
		score = cc.compareWithClasses(test_data,indexImg,classes[:,:,i])
		if (i==0):
			min = score
			indMin = 0
		elif (score < min):
			min = score
			indMin = i
	return indMin

