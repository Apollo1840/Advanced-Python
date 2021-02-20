# tree depth
# point: dynamic programming

# way 1 (98)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode):
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


# make balanced Tree
def makeBST(nums, start, end):
    if end == start:
        return
    index = start + (end - start) // 2
    new_node = TreeNode(nums[index])
    new_node.left = makeBST(nums, start, index)
    new_node.right = makeBST(nums, index + 1, end)
    return new_node


nums = [1, 2, 3, 1, 2, 3, 2, 2, 2, 3, 1, 0]
makeBST(nums, 0, len(nums))


# slower
class Solution:
    def sortedArrayToBST(self, nums):
        def makeBST(nums):
            if not nums:
                return
            mi = len(nums) // 2
            new_node = TreeNode(nums[mi])
            new_node.left = makeBST(nums[:mi])
            new_node.right = makeBST(nums[(mi + 1):])
            return new_node

        return makeBST(nums)


# House Robber
# maxmize sum, but no adjacenet data acquire

class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp.pop()


class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        return max(self.rob(nums[:-1]), self.rob(nums[:-2]) + nums[-1])


class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        rob1 = nums[0]
        rob2 = max(nums[:2])
        for num in nums[2:]:
            temp = rob2
            rob2 = max(rob1 + num, rob2)
            rob1 = temp
        return rob2


s = Solution()
s.rob([1, 8, 3, 4, 10, 2])

