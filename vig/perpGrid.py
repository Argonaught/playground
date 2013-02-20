#! /usr/bin/python
import string
def grid(cipherText, width):

	res=''
	rows = []
	for i in range(width):
		rows.append('')
	i = 0
	for i in range(0, len(cipherText)):
		c = (cipherText[i])
		if c == '\n':
			c='N'
		rows[i%width] += c
		
	for row in rows:
		print(string.join(row))

