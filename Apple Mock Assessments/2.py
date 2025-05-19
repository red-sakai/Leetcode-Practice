"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]

Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
"""

class Solution:
    def findDisappearedNumbers(nums: list[int]) -> list[int]:
        n = len(nums)
        num_set = set(nums)
        return [i for i in range(1, n + 1) if i not in num_set]
    
# test cases
print(Solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # [5, 6]
print(Solution.findDisappearedNumbers([1,1]))  # [2]
print(Solution.findDisappearedNumbers([1, 2, 3, 4, 5]))  # []
print(Solution.findDisappearedNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # []