#! /usr/bin/python

from nltk.probability import FreqDist
def xorByAlpha(alphas, cipherText, common):
	key = []
	for alpha in alphas:
		fdist = FreqDist(alpha)
		kxor = (ord(fdist.max()) ^ ord(common))
		key.append(kxor)

	keyLen = len(key)
	res = ''
	for i in range(0, len(cipherText)):
		c = chr((ord(cipherText[i]) ^  key[i%keyLen]))
		res += c

	print (res)
