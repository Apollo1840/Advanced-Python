
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



## Python Point

you can also see `python_leetcode.ipynb`

### Point 1:  reversed string
do not use 
    
    s_r = reversed(s)             # it will return a list, you need:
    s_r = ''.join(reversed(s))        

instead we use 

    s_r = s[::-1]
    
bonus:

    print(s[3] )            # this is working
    print(s[::2])           # also
   

### Point 2: range details

range with left without right.

- range(n) :  [0, 1, ..., n-1]
- range(0, n): = range(n)
- range(1, n) :  [1, ..., n-1]
- range(1, n+1): [1, ..., n]

### Point 3: use "is None"


### Point 4: List index and count
a = [1,2,3,4,5]

- a.index(6) will raise error
- a.count(6) will not

### Point 5: dictionary pop

    dikt.pop(i)
    dikt.popitem()[0]

### Point 6: dictionary.keys()

dictionary.keys() is not a list


### Point 7: ord() and chr()
ord() gives the code of a char.

python build-in : https://docs.python.org/2/library/functions.html


### Point 8: for-else

if the for loop does not 'break' then run else

    for chance in [1,3,2,4]:
        if chance == 4:
            print("win")
            break
    else:
        print("lose")

### Point 9: min or
It will first check can first list gives a min, if not, find the min of next one

    print(min([] or [-1,-2]))       #  -2
    print(min([2,3,4] or [-1,-2]))  #  2

### Point 10: *list

*lst break the list into several inputs


## Tools (python build-in)


### Tools 1: collections.Counter

    from collections import Counter
    
    nums = [1,1,1,2,2,2,2,2,3,3,4,5,5,5]
    
    c = Counter(nums)
    print(c)
    print(c.most_common(2))  # List[tuple]: (num, count)


### Tools 2: itertools.group

    import itertools 
    
    for digit, group in itertools.groupby('112223331112223333'):
        print(digit, list(group))
        
    # output (1, 11), (2, 222),(3,333), 1,111 ...
