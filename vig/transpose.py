#! /usr/bin/python
import string
def transpose(cipherText, key):
	kLen = len(key)
	i = 0
	res = ''
	while i < len(cipherText):
		group = cipherText[i:(i + kLen) % len(cipherText)]
		print('cipher group' + group)
		tmp = []
		for pos in key:
			if pos < len(group):
				tmp.append(group[pos])
		res += string.join(tmp)
		print(res)
		i += kLen
	print (res)
