#! /usr/bin/python

from nltk.probability import FreqDist
def shiftByAlpha(alphas, cipherText, common):
	key = []
	for alpha in alphas:
		fdist = FreqDist(alpha)
		#shift = (ord(fdist.max()) - ord(common))
		shift = (ord(common) - ord(fdist.max()))
		key.append(shift)

	keyLen = len(key)
	res = ''
	for i in range(0, len(cipherText)):
		c = chr((ord(cipherText[i]) + key[i%keyLen])%128)
		res += c

	print (res)
