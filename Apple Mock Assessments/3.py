"""
Given integers n and k, return the kth largest integer in the array nums.
If two integers are equal, the first one is considered the largest.

Example 1:
Input: n = 5, k = 2, nums = [3, 1, 4, 1, 5]
Output: 4

Example 2:
Input: n = 5, k = 3, nums = [3, 1, 4, 1, 5]
Output: 3

Example 3:
Input: n = 5, k = 1, nums = [3, 1, 4, 1, 5]
Output: 5
"""

class Solution:
    def kthLargest(n: int, k: int, nums: list[int]) -> int:
        nums.sort(reverse=True)
        return nums[k - 1] if k <= n else -1

# test cases
print(Solution.kthLargest(5, 2, [3, 1, 4, 1, 5]))  # 4
print(Solution.kthLargest(5, 3, [3, 1, 4, 1, 5]))  # 3
print(Solution.kthLargest(5, 1, [3, 1, 4, 1, 5]))  # 5