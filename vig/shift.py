#! /usr/bin/python

from nltk.probability import FreqDist
def shiftByAlpha(alphas, cipherText, common, reverse):
	key = []
	for alpha in alphas:
		fdist = FreqDist(alpha)
		if reverse:
			shift = (ord(common) - ord(fdist.max()))
		else:
			shift = (ord(fdist.max()) - ord(common))
		key.append(shift)
		print('shift ' + str(shift))

	keyLen = len(key)
	res = ''
	for i in range(0, len(cipherText)):
		c = chr((ord(cipherText[i]) + key[i%keyLen])%128)
		res += c

	print (res)
