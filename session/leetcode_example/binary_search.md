# Implementing binary search

## A trival way

A simple and easy implementation is to enable mid-out, left-out and right-out.
namely, while condition is `left < right - 1`. 
and left and right could be set to mid on every iteration if it meeting the target condition.
finally, we will check `a[left], a[right], and a[mid]`.

## Based on left-forward

If `left = mid + 1`, the search process can lead to `left == right` after several rounds of iteration.
This enables another implementation of Binary Search, which I called **left-across BS(LaBS)**.

LaBS is naturally suitable for argmin search:

```math
- argmin a[i] >= t
- argmin a[i] > t  (this is equal to argmin a[i]>= t+1, if a[i] are ints)
```


In LaBS, while condition is `while left < right`. 
and `left = mid + 1` when `a[left]` not meet the target condition.

Take the outcome of LaBS, called `y`. you could simply use `y-1` as the outcome of:

```math
- argmax a[i] < t
- argmax a[i] <= t
```

So far, you could solve all types of binary search. 
And if `a[i]` are ints, you could implement them all based on `argmin a[i] >= t`.

For example, `int(sqrt(x))` is simply `argmax i**2 <= t`, and equal to `(argmin i**2 >= t+1) - 1`

```python

def mySqrt(x: int) -> int:
    l, r = 0, x + 1   # x + 1 to deal with the case that x == 0.
    while l<r:
        mid = (l+r)//2
        # if mid**2 == x:
        #   return mid
        if mid**2 >= x+1:
            r = mid
        else:
            l = mid + 1
    return l - 1


```



