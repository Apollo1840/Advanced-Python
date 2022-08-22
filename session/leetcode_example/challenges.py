# -----------------------------------------------
# Intersection of Two Arrays II
# Given two arrays, write a function to compute their intersection.

class Intersection_of_Two_Arrays_II(object):
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


s = Intersection_of_Two_Arrays_II()
s.intersect([4, 9, 5], [9, 4, 9, 8, 4])


# -----------------------------------------------
# Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Merge_Two_Sorted_Lists:
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

class Pascal_Triangle:
    def generate(self, numRows):

        def Pt(a):
            b = []
            for i in range(len(a) - 1):
                b.append(a[i] + a[i + 1])
            return b

        if numRows == 0: return []
        res = [[1]]
        for i in range(numRows - 1):
            res.append([1] + Pt(res[i]) + [1])
        return res


class Pascal_Triangle:
    def generate(self, numRows):
        pt = lambda a: [a[i] + a[i + 1] for i in range(len(a) - 1)]
        res = [[1]]
        for i in range(numRows - 1):
            res.append([1] + pt(res[i]) + [1])
        return res


class Pascal_Triangle:
    def generate(self, numRows):
        def pt(a):
            mid = len(a) // 2
            if len(a) % 2 == 0:
                b_half = [a[i] + a[i + 1] for i in range(mid - 1)]
                return b_half + [a[mid - 1] + a[mid]] + list(reversed(b_half))
            else:
                b_half = [a[i] + a[i + 1] for i in range(mid)]
                return b_half + list(reversed(b_half))
        res = [[1]]
        for i in range(numRows - 1):
            res.append([1] + pt(res[i]) + [1])
        return res


# -----------------------------------------------
# Symmetric Tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

class Symmetric_Tree:
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


class Symmetric_Tree:
    def isSymmetric(self, root):
        def isSym(left, right):
            if left and right:
                return left.val == right.val and isSym(left.left, right.right) and isSym(left.right, right.left)
            else:
                return left is right

        return isSym(root.left, root.right)


# -----------------------------------------
# Balance Tree
# trick: recursive at the same time

class Balance_Tree:
    def isBalanced(self, root):
        def check(node):
            if node is None:
                return 0, True
            l_depth, l_balanced = check(node.left)
            r_depth, r_balanced = check(node.right)
            return max(l_depth, r_depth) + 1, l_balanced and r_balanced and abs(l_depth - r_depth) <= 1

        return check(root)[1]


# ----------------------------------------------------
# Number of 1 Bits
# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight). 

class Number_of_1_Bits(object):
    def hammingWeight(self, n):
        sum1 = 0
        while n:
            sum1 += n % 2
            n = n // 2
        return sum1


# -----------------------------------------------
# Linked List Cycle
# Given a linked list, determine if it has a cycle in it.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Linked_List_Cycle(object):
    def hasCycle(self, head):
        fast = slow = head

        while slow and fast and fast.next:
            slow = slow.next  # Step of 1
            fast = fast.next.next  # Setp of 2

            if slow is fast:  # Checking whether two pointers meet
                return True

        return False


# -----------------------------------------------
# Palindrome Linked List
# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Palindrome_Linked_List(object):
    def isPalindrome(self, head):
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # the mid node is slow
        print("mid", slow.val)

        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        # compare the first and second half nodes
        while node:  # while node and head: (the node must be the shorter one)
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True


ln0 = ListNode(1)
ln1 = ListNode(2)
ln2 = ListNode(2)
ln3 = ListNode(1)
ln0.next = ln1
ln1.next = ln2
ln2.next = ln3
s = Palindrome_Linked_List()
s.isPalindrome(ln0)


# -----------------------------------------------
# Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack(object):

    def __init__(self):
        self.stack = [(-1, float('inf'))]

    def push(self, x):
        self.stack.append([x, min(x, self.stack[-1][1])])

    def pop(self):
        if len(self.stack) > 1: self.stack.pop()

    def top(self):
        if len(self.stack) == 1: return None
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


# ----------------------------------------------------
# Sqrt(x)

class Sqrt(object):
    def mySqrt(self, x):
        l, r = 0, x
        while l < r:
            mid = (l + r) // 2
            if x < mid * mid:
                r = mid
            else:
                l = mid + 1
        return l - 1 if l > 1 else l
