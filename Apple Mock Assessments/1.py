"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two if there exists an integer x such that n == 2^x.

Example 1:
Input: n = 1
Output: true
Explanation: 2^0 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 2^4 = 16
"""

class Solution:
    def isPowerOfTwo(n: int) -> bool:
        power = 1
        while power <= n:
            if power == n:
                return True
            power *= 2
        return False
    
# test cases
print(Solution.isPowerOfTwo(1))  # True
print(Solution.isPowerOfTwo(16))  # True
print(Solution.isPowerOfTwo(3))  # False