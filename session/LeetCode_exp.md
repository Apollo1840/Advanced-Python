
## Tech

### Tech 1: Recurence and DP
There is a kind of problem, in this kind of problem, if we can solve small scale version we can solve a bigger one.
I call it DP problem. such as:

* Tree deepth
* ...

### Tech 2: Hashtable
Set a dictionary as alternative storage to solve your problem.







## Point

### Point 1:  reversed string
do not use reversed(s), it will return a list, you need ''.join(reversed(s))        
instead we use s[::-1]
    
bonus:
   str1[3] is working 
   str1[::2] also
   

### Point 2: range details
range with left without right.
range(n) :  [0, 1, ..., n-1]
range(0, n): range(n)
range(1, n) :  [1, ..., n-1]
range(1, n+1): [1, ..., n]

### Point 3: use "is None"



### Point 4: List index
a = [1,2,3,4,5]
a.index(6) will raise error
a.count(6) will not

### Point 5: dictionary pop
dikt.pop(i)
dikt.popitem()[0]


### Point 6: dictionary.keys()
It is not a list


### Point 7: ord() and chr()
ord() gives the code of a char.

python build-in : https://docs.python.org/2/library/functions.html


### Point 8: counts
import collections
counts = collections.Counter(nums)
counts.most_common(1) returns a list of couple (num, freq)


### Point 9: min or
It will first check can first list gives a min, if not, find the min of next one
min([] or [-1,-2])  
min([2,3,4] or [-1,-2])




