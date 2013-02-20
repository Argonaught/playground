#! /usr/bin/python

def grid(cipherText, width):

	res=''
	for i in range(0, len(cipherText)):
		c = (cipherText[i])
		if c == '\n':
			c='N'
		res += c
		if (i + 1) % width == 0:
			print( res )
			res = ''

