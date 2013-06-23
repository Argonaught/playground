exercise one.

Algorithm Performance

Let's say we want to measure the performance of an algorithm. One way you could do it is to run it and time it.
given a list of 10 integers it takes 10 seconds to sort it. So we might be tempted to say that it takes 1 second per integer in the list

Wrong...

If sorting 10 items takes 10 seconds sorting 100  will not take 100 seconds. Most likely it will take 1000 

So our timing test is not particularly useful because because it only tells us how our algorithm performs under specific circumstances.


Complexity

a better measure is the Complexity: 

No need to memerise this bit, just to get the jist...


The lowest Complexity and alogorithm can have is Constant or O(1)
	this means that it takes the same number of operations (and therefore time you would hope) to complete regardless of how many how many items in the list  
	10 items 10 seconds 100 items 10 seconds
	no such thing as O(2,3,4, etc) btw


The next level is logarithmic or O(log n)
	This means the number of operations goes up by the log of n. 10 items 10 seconds 100 items 20 seconds ( I think ) 
	
The next level is Linear or O(n)
	This means that the number of operations required is proportional to the number of items in the list. so 10 items 10 seconds 100 items 100 seconds


The next level is linearithmic time or O(n log n) 
	Looks a little wierd but same as O(log n) multiplied by n. so 10 items 10 seconds 100 items 200 seconds

The next level is quadratic time or O(n^2)
	This means the number of operations goes up by the square of the number of items. You will come across a lot. moveing towards the problematic complexities now, because...
	10 items 10 seconds 100 items 1000 seconds, 1000 items 100000 seconds.

the next level is cubic or O(n^3)
	Similar to the above. we can keep going down this path and get O(n^4) O(n^5) etc etc. 

The next level is factorial time or O(n!)
	A whole new level pain. 5 items 120 seconds 100 items  9*10^157 seconds or 3*10^138 billion years. 
	if you ran this at the time of the big bang you'd still be waiting. check out the trading salesman problem 

There are obviosly far more than this, but this is what you're going to come across regularly.



CODING:
in ex1.py implement mySort(arry)

it should return the given array sorted (ascending or descending)

2 hours
1.Try to do it in quadratic time first O(n^2).

This should be simple, but the next part is more challenging 	

4 hours
2. make the sorting work in linearithmic time O(n log n)
hint: there are two well known algorithms that do this. one has quick in the name. the other has merge.

bonus points for implementing both algorithms.

8 hours
3. Only for the hard core: Research and explain a complexity from here: http://en.wikipedia.org/wiki/Time_complexity that:
	a. is not in the list above and...
	b. does not have the work exponential in it

	I don't know the answer myself so references please. Something like a 1 page essay. Good practice...
	I have no idea what any 

 
