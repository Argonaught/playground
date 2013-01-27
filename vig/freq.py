#! /bin/usr/python2

import nltk
from nltk.tokenize import *
from nltk.probability import FreqDist
import argparse
import sys

def main():
        argparser = argparse.ArgumentParser(description='text file')
        argparser.add_argument('file', type=str, help='file to produce frequency distribution for')
        args = argparser.parse_args()
        
	#toker = WhitespaceTokenizer()

	f = open(args.file)
	text = f.read()
	print(text)
	fdist = FreqDist(text)
	print(fdist.freq('28') * 100)
	fdist.plot()

if __name__ == "__main__":
        main()

