#! /usr/bin/python

def splitByAlpha(nAlpha, cipherText):
	array = []
	for i in range(0, nAlpha):
		group = ''
		array.append(group)

	i = 0
	while i < len(cipherText):
		array[i % nAlpha] += cipherText[i]
		i += 1
	return array
	

