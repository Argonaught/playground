#! /bin/usr/python2

import nltk
from nltk.tokenize import *
from nltk.collocations import *
from nltk.probability import FreqDist
import argparse
import sys
import string
import findKey
import split
import myFreqDist
import shift
import xor
import grid
import transpose
import perpGrid
def main():
        argparser = argparse.ArgumentParser(description='text file')
        argparser.add_argument('file', type=str, help='file to produce frequency distribution for')
	argparser.add_argument('-m', '--pLen', type=int, default=4, help='length of the patterns to look for')
	argparser.add_argument('-n', '--nRes', type=int, default=5, help='number of results to show')
	argparser.add_argument('-k', '--findKey', help='find patterns from repeating key', action='store_true')
	argparser.add_argument('-p', '--plotByAlpha', help='-p N: split cipher text by N alphabets and save plots. specify dir to save with -d. default is the current directory', type=int, default=0)
	argparser.add_argument('-l', '--cipherLen', help='display the length of the cipher text', action='store_true')
	argparser.add_argument('-d', '--outDir', type=str, default='.', help='directory to save files to')
	argparser.add_argument('-a', '--ascii', help='text is ascii', action='store_true')
	argparser.add_argument('-s', '--shiftByAlpha', help='-s N: split cipher text by N alphabets and shift on the basis of frequency analysis', type=int, default=0)
	argparser.add_argument('-r', '--reverseShift', help='shift charcters backwards', action='store_true')
	argparser.add_argument('-x', '--xorByAlpha', help='-x N: split cipher text by N alphabets and xor on the basis of frequency analysis', type=int, default=0)
	argparser.add_argument('-c', '--common', help='most common letter in plain text alphabet', default='e')
	argparser.add_argument('-g', '--grid', help='-g N: output the cipher text in a grid N chars wide', type=int, default=0)
	argparser.add_argument('-t', '--transpose', help='-t N: output the cipher text in a grid N chars wide', metavar='N', nargs='+', type=int, default=0)
	argparser.add_argument('-i', '--perpGrid', help='-g N: output the cipher text in a grid N chars wide', type=int, default=0)

        args = argparser.parse_args()
        
	toker = WhitespaceTokenizer()

	f = open(args.file)
	if args.ascii:
		text = f.read().split()
		arry = []
		for e in text:
			arry.append(chr(int(e, 16)))
		#ascString = string.join(arry)
		ascString = arry
	else:
		ascString = f.read()
		tmp = ''
		for c in ascString:
			if ord(c) < 128:
				tmp = tmp + c

		ascString = tmp	
	if args.cipherLen:
		print('cipher text length: ' + str(len(ascString)))
	
	if args.findKey:
		print(findKey.getNgramsDispersion(string.join(ascString), args.pLen, args.nRes))

	if args.plotByAlpha > 0:
		alphas = split.splitByAlpha(args.plotByAlpha, ascString)
		g = 0
		for group in alphas:
			g += 1
			myFreqDist.MyFreqDist(group).createPlot(args.outDir + 's' + str(args.plotByAlpha) + 'g' + str(g), 10)

	if args.shiftByAlpha > 0:
		alphas = split.splitByAlpha(args.shiftByAlpha, ascString)
		candidate = shift.shiftByAlpha(alphas, ascString, args.common, args.reverseShift)
		file = open(args.outDir + 'candidate.pln', 'w')
		print(candidate) 
	
	if args.xorByAlpha > 0:
                alphas = split.splitByAlpha(args.xorByAlpha, ascString)
                candidate = xor.xorByAlpha(alphas, ascString, args.common)
                file = open(args.outDir + 'candidate.pln', 'w')
                print(candidate)

	if args.grid > 0:
		grid.grid(ascString, args.grid) 

        if args.perpGrid > 0:
                perpGrid.grid(ascString, args.perpGrid)

	if len(args.transpose) > 0:
		transpose.transpose(ascString, args.transpose)

if __name__ == "__main__":
        main()

