# -----------------------------------------------
# Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

class Solution(object):
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

  



# -----------------------------------------------
# Linked List Cycle
# Given a linked list, determine if it has a cycle in it.

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        fast = slow = head

        while slow and fast and fast.next:
            slow = slow.next                # Step of 1
            fast = fast.next.next           # Setp of 2

            if slow is fast:                # Checking whether two pointers meet
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

class Solution(object):
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
        while node: # while node and head: (the node must be the shorter one)
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
s = Solution()
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
         
class Solution(object):
    def mySqrt(self, x):
        l,r = 0,x
        while l < r:
            mid = (l+r) // 2
            if x < mid*mid:
                r = mid
            else:
                l = mid + 1
        return l-1 if l>1 else l
