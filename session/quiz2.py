# -----------------------------------------------
# Intersection of Two Arrays II
# Given two arrays, write a function to compute their intersection.

class Solution(object):
    def intersect(self, nums1, nums2):
        d = {}
        result = []
        
        # build up the dict of number
        # counts from the first list
        for num in nums1:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        # check if the numbers in the
        # second list occur in the dict
        for num in nums2:
            if num in d:
                if d[num] > 0:
                    d[num] -= 1
                    result.append(num)
                    
        return result
    
s = Solution()
s.intersect([4,9,5],[9,4,9,8,4])



# -----------------------------------------------
# Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
    
        if (l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

# -----------------------------------------------
# Pascal's Triangle
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

class Solution:
    def generate(self, numRows):
        
        def Pt(a):
            b = []
            for i in range(len(a)-1):
                b.append(a[i] + a[i+1])
            return b
        
        if numRows==0: return []
        res = [[1]]
        for i in range(numRows-1):
            res.append([1] + Pt(res[i]) + [1])
        return res

# -----------------------------------------------
# Symmetric Tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
        
class Solution:
    def isSymmetric(self, root):
        if root is None:
          return True
        else:
          return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
          return True
        if left is None or right is None:
          return False

        if left.val == right.val:
          outPair = self.isMirror(left.left, right.right)
          inPiar = self.isMirror(left.right, right.left)
          return outPair and inPiar
        else:
          return False

# ----------------------------------------------------
# Number of 1 Bits
# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight). 
         
class Solution(object):
    def hammingWeight(self, n):
        sum1 = 0
        while n:
            sum1 += n%2            
            n = n//2
        return sum1
