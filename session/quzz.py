# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 19:01:32 2018

@author: zouco
"""

# reverse string
# way 1 (85)
def reverse_string(s):
    return ''.join(reversed(s))

str1 = 'abc'
str2 = 'hallo world'
reverse_string(str1)
reverse_string(str2)

# way 2 (85)
# know: 
def reverse_string(s):
    return s[::-1]

'''
    str1[3] is working 
    str1[::2] also
'''


# FizzBuzz
# way1 (98)
mask = lambda i: 'Fizz'*(i%3 == 0)+'Buzz'*(i%5==0)
n = 20 
res = []
for i in range(1,n+1):
    if i%3 != 0 and i%5!=0:
        res.append(str(i))
    else:
        res.append(mask(i))
print(res)


'''
    range(n) :  [0, 1, ..., n-1]
    range(0, n)
    range(1, n) :  [1, ..., n-1]
    range(1, n+1): [1, ..., n]
    
'''


# tree depth 
# way 1 (98)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


'''
    use 'is None'
    
'''       


# find single item

# way 1 (25)
def find_single(nums):
    hash_table = {}
    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1
    return hash_table.popitem()[0]

# way 2 (faster)
def find_single2(nums):
    hash_table = {}
    for i in nums:
        if i in hash_table.keys():
            hash_table.pop(i)
        else:
            hash_table[i] = 1
    return list(hash_table.keys())[0]

# I dont understand
def find_single3(nums):
    res = nums[0]
    for i in range(1, len(nums)):
        res = res ^ nums[i]
    return res 
           
lst = [1,4,2,2,3,1,5,3,4]
lst2 = [2,2,1]
lst3 = [1,0,1]
find_single(lst3)
    
'''
    index will raise error when there is no such elements in the list
    list.count(1)
    
    dikt.pop(i)
    dikt.popitem()[0]
    dikt.keys() is not a list
'''


# move zero to the end

# way 1 (28)
def move_zero(nums):
    num_zero = 0
    len_nums = len(nums)
    for i in range(len_nums):
        if nums[i-num_zero] == 0:
            nums.pop(i-num_zero)
            nums.append(0)
            num_zero += 1


def move_zero2(nums):        
    t=0
    while 0 in nums:
        for i, num in enumerate(nums):
            if nums[i] == 0:
                del nums[i]
                t += 1         #keep track of the "0's" we delete
    for j in range(t):
            nums.append(0)      #add them back to the end of the array
            
      
def move_zero3(nums): # last_zero means first zero position           
    last_zero = 0
    curr = 0
    while curr < len(nums) and last_zero < len(nums):
        if nums[curr] != 0:
            nums[last_zero], nums[curr] = nums[curr], nums[last_zero]
            last_zero += 1
        curr += 1


nums = [1,4,2,0,0,3,0,5,0,4]
move_zero3(nums)
print(nums)

'''
    do not affect the loop condition

'''





# reverse link

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev