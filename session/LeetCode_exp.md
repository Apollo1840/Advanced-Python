
## Tech

### Tech 1: Recurence and DP
There is a kind of problem, in this kind of problem, if we can solve small scale version we can solve a bigger one.

I call it DP problem. such as:

* Tree deepth
* Make balance Tree
* 1,2 step to end
* rob
* ...

### Tech 2: Hashtable
Set a dictionary as alternative storage to solve your problem.

For example:
* two sum








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


### Point 8: for else
if the for loop do not 'break' then run else


### Point 9: min or
It will first check can first list gives a min, if not, find the min of next one

min([] or [-1,-2])  

min([2,3,4] or [-1,-2])

### Point 10: *list
lst = [[1,2,3],[4,5,6]]

list(zip(*lst))






## Tools


### Tools 1: collections.Counter
counts = collections.Counter(nums)

counts.most_common(1) returns a list of couple (num, freq)

### Tools 2: itertools.group
for digit, group in itertools.groupby('112223331112223333'):

digit, list(group):

output (1, 11), (2, 222),(3,333),1,111 ...
