'''Given an unsorted array A of size N that contains only non negative integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.
Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.'''

------------------------------------------------------------------------------------
class Solution:
    def subArraySum(self, arr, n, s):
        for j in range(n):
            sum = 0
            for k in range(j, n):
                sum += arr[k]
                if sum == s:
                    return [j + 1, k + 1]  # Return the indices of the subarray (1-based indexing)
                elif sum > s:
                    break
        return [-1]  # If no subarray with sum s is found, return [-1]

# Example usage:
solution = Solution()
arr = [1, 2, 3, 7, 5]
n = len(arr)
s = 12
print(solution.subArraySum(arr, n, s))  # Output: [2, 4]
