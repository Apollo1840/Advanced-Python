# -*- coding: utf-8 -*-

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
    Point 1:  reversed string
    do not use reversed(s), it will return a list, you need ''.join(reversed(s))        
    instead we use s[::-1]
    
    bonus:
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
            
      
'''
    ***** hard *****
'''        
        
def move_zero3(nums):        
    curr = 0       # curr will keep forward until it meets nonzero
    last_zero = 0  # at first, it is same as curr then it means the first zero position 
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




'''
    ***** hard *****
'''  

# reverse link

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def reverseList(self, head):
        prev = None
        while head:
            temp = head        # temp has get the id of the header and prev save the id of the temp
            head = head.next   # because we going to change temp so we need to assign a new id to head first      
            temp.next = prev         
            prev = temp
        return prev
    
head = ListNode(0)
one = ListNode(1)
two = ListNode(2)
three = ListNode(3)

head.next = one
one.next = two
two.next = three

s = Solution()
rev = s.reverseList(head)

print(rev.val)
print(rev.next.val)
print(rev.next.next.val)
print(rev.next.next.next.val)




# Excel column to number

# (41)
class Solution:
    def titleToNumber(self, s):
        num_c = 0
        i = 1
        for c in reversed(s):
            num_c += (ord(c)-64)*i
            i=i*26
            
        return num_c
    
    
    
# most appearance
import collections
nums = [1,2,3,1,2,3,2,2,2,3,1,0]
counts = collections.Counter(nums)
print(counts.most_common(1)[0][0])





'''
    ***** trick *****
'''  
# best time buy and sale

prices = [1,7,3,4,5,3,2,3,2,]
sum([prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]>prices[i]])




'''
    ***** trick *****
''' 

# in order traversal

# (39)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        return [] if (root is None) else self.inorderTraversal(root.left) + [root.val] +  self.inorderTraversal(root.right) 



# reverse digits in integer
class Solution:
    def reverseDigits(self, x):  # this one is faster.   
        is_int32 = lambda x : -0x80000000 <= x <= 0x7FFFFFFF
        if is_int32(x):
            if x >=0:
                res = int(str(x)[::-1])
                if is_int32(res):
                    return res
            else:
                res = int('-'+str(-x)[::-1]) 
                if is_int32(res):
                    return res
        return 0
    
    def reverseDigits2(self, x):
        is_int32 = lambda x : -0x80000000 <= x <= 0x7FFFFFFF
        reverse_int = lambda x: int(str(x)[::-1]) if x>0 else int('-'+str(-x)[::-1])
        if is_int32(x):
            res = reverse_int(x)
            if is_int32(res):
                return res
        return 0




'''
    ***** trick *****
''' 
import math
def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    
    # even no
    if n > 2 and n%2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n%d == 0:
            return False

    return True

# count prime
def countPrimes(n):
    if n <= 2: # exclude 0 and 1, make sure primes[0] and primes[1] is callable
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])  # this is faster than for loop
    return sum(primes)





# anagram
s='abcdss'
t='dsascb'
collections.Counter(list(s)) == collections.Counter(list(t))


# contain duplicates
nums = [1,2,3,1]
len(nums) != len(set(nums))


class Solution:
    def firstUniqChar(self, s):

        list_res = []
        list_duplicate = []
        for c in s:
            if len(list_res)==1 and c not in s[(s.find(c)+1):]:
                return c
            else:
                list_res.remove(c)
                list_duplicate.append(c)

            if c in list_duplicate:
                pass
            elif c in list_res:
                list_res.remove(c)
                list_duplicate.append(c)
            else:
                list_res.append(c)
        return list_res[0]

# 28
class Solution:
    def firstUniqChar(self, s):
        if not s:
            return -1
        list_res = []      
        list_duplicate = []
        for c in s:
            if c in list_duplicate:
                continue
            elif c in list_res:
                list_res.remove(c)
                list_duplicate.append(c)
            else:
                list_res.append(c)
        if not list_res:
            return -1
        else:
            print(list_res[0])
            return s.find(list_res[0])

s = Solution()
s.firstUniqChar('abcbc')


# answer
min([s.index(char) for char in set(s) if s.count(char) == 1] or [-1])

'''
    min([] or [-1])
    min([2,3,4] or [-1])

'''





# make balanced Tree
def makeBST(nums, start, end):
    if end == start:
        return
    index = start + (end - start) // 2
    new_node = TreeNode(nums[index])
    new_node.left = makeBST(nums, start, index)
    new_node.right = makeBST(nums, index+1, end)
    return new_node

makeBST(nums, 0, len(nums))

# slower
class Solution:
    def sortedArrayToBST(self, nums):
        def makeBST(nums):
            if not nums:
                return
            mi = len(nums)//2
            new_node = TreeNode(nums[mi])
            new_node.left = makeBST(nums[:mi])
            new_node.right = makeBST(nums[(mi+1):])
            return new_node
        return makeBST(nums)
    
    
    
# Two Sum
# [2,7,9,11] 
def twosum(nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}  # {7:1}
    for i in range(len(nums)):
        if nums[i] not in buff_dict:
            buff_dict[target - nums[i]] = i
        else:
            return [buff_dict[nums[i]], i]
    return False



# plus one
digits = [1,2,3]
[int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)] 

class Solution:
    def plusOne(self, digits):
        i = 0
        while True:
            if len(digits)-i-1 >= 0:
                if digits[-i-1] + 1 < 10:
                    digits[-i-1] += 1
                    return digits
                else:
                    digits[-i-1] = digits[-i-1] - 9
                    i += 1
            else:
                return [1]+digits


'''
    trick : check last 9
'''

        
'''
   itertools..

'''
import itertools
for digit, group in itertools.groupby('112223331112223333'):
    print(digit)
    print(list(group))


#  how mang ways to the end
# DP
class Solution:
    def climbStairs(self, n):
        if n==1:
            return 1
        dp = [1,2]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp.pop()


class Solution:
    def rob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        return max(self.rob(nums[:-1]), self.rob(nums[:-2])+nums[-1])
    

class Solution:
    def rob(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        rob1 = nums[0]
        rob2 = max(nums[:2])
        for num in nums[2:]:
            temp = rob2           
            rob2 = max(rob1 + num, rob2)
            rob1 = temp            
        return rob2
    

s=Solution()
s.rob([1,8,3,4,10,2])



class Solution:
    def longestCommonPrefix(self, strs):
        i = 0
        while(True): 
            for sstr in strs:
                if i >= len(sstr):
                    break
                elif sstr[i]!=strs[0][i]:
                    break
            else:
                i+=1
                continue
            break
        return strs[0][:i]   

s=Solution()
s.longestCommonPrefix(['flo',"flower","flow","flowight"])  


lst = [[1,2,3],[4,5,6]]
list(zip(*lst))



class Solution:
    def longestCommonPrefix(self, strs):       
        shortest = min(strs, key = len)
        for i in range(len(shortest)): 
            for sstr in strs:
                if sstr[i]!=strs[0][i]:
                    break
            else:
                i+=1
                continue
            break
        return strs[0][:i]   
    
    
    
    
    
class Solution:
    def isPalindrome(self, s):
        
        lst = [c.lower() for c in s if (97 <= ord(c) <= 122 or 65 <= ord(c) <= 90)]
        print(lst)
        index = len(lst)//2
        print(index)
        s1 = ''.join(reversed(lst[:index]))
        s2 = ''.join(lst[index+len(lst)%2:])
        print(s1)
        print(s2)
        return s1 == s2
s=Solution()
s.isPalindrome('OP') 







symbol = ['I','V','X','L','C','D','M']
symbol_value = [1,5,10,50,100,500,1000]
valid_double = []
for i in range(0,6,2):
    valid_double.extend([symbol[i]+symbol[i+1],symbol[i]+symbol[i+2]])
valid_double_value=[4,9,40,90,400,900]

def romanToInt(s):
    if len(s)==0:
        return 0
    elif len(s)==1:
        return symbol_value[symbol.index(s)]
    elif s[:2] in valid_double:
        return valid_double_value[valid_double.index(s[:2])] + romanToInt(s[2:])
    else:
        return symbol_value[symbol.index(s[0])] + romanToInt(s[1:])
    

romanToInt('XIV')

def romanToInt(s):
    if len(s)==0:
        return 0
    
    else:
        roman_dict = {'I':1, 'V':5,'X':10, 'L':50,'C':100,'D':500,'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        if len(s)==1:
            return roman_dict[s]
        elif s[:2] in roman_dict.keys():
            return roman_dict[s[:2]] + romanToInt(s[2:])
        else:
            return roman_dict[s[0]] + romanToInt(s[1:])


class Solution:
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    
    def romanToInt(self, s):
        z = 0
        for i in range(0, len(s) - 1):
            z += self.roman[s[i]]*(-1 if self.roman[s[i]] < self.roman[s[i+1]] else 1)
        return z + self.roman[s[-1]]
    
    
        # return sum([self.roman[s[i]]*(-1 if self.roman[s[i]] < self.roman[s[i+1]] else 1) for i in range(0, len(s) - 1)]) + self.roman[s[-1]]