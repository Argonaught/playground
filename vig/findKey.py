#! /usr/bin/python2

import string

def getNgramsDispersion(ascString, plen, nRes):
	patterns = []

        for i in range(0, len(ascString) - plen):
                curPattern = ascString[i:i+plen]
                index = string.find(ascString, curPattern)
                count = 0
                distances = []
                while index > -1:
                        count += 1
                        nextIndex = string.find(ascString, curPattern, index + 1)
                        distances.append(nextIndex - index)
                        index = nextIndex
                tup = (curPattern, count, distances)
                patterns.append(tup)
        scored = sorted(patterns, key=lambda tup: tup[1], reverse = True)
        return scored[0:nRes]

