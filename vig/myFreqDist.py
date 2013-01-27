#! /usr/bin/python2

from nltk.probability import FreqDist

class MyFreqDist(FreqDist):
	def createPlot(self, file, *args, **kwargs):
		try:
			import pylab
		except ImportError:
			raise ValueError('missing pylab')
		samples = super(MyFreqDist, self).samples()
		freqs = [self[sample] for sample in samples]
		ylabel = 'Counts'

		pylab.grid(True, color='Silver')
		pylab.plot(freqs, **kwargs)
		pylab.xticks(range(len(samples)), [ord(s) for s in samples], rotation=90)
		pylab.xlabel('Samples')
		pylab.ylabel('Counts')
		pylab.savefig(file)
