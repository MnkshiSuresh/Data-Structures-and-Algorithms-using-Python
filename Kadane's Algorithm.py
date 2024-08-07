'''Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.


Example:

Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.'''

--------------------------------
class Solution:
    def maxSubArraySum(self,arr,N):
        larger = arr[0] # Initialize the variable to store the maximum sum
        current_sum = arr[0] # Initialize the variable to store the current sum
        
        for i in range(1, N): # Start iterating from the second element
            current_sum = max(arr[i], current_sum + arr[i]) # Update the current sum
            larger = max(larger, current_sum) # Update the maximum sum
        
        return larger # Return the maximum sum

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, -2, 5]
    N = len(arr)
    sol = Solution()
    print(sol.maxSubArraySum(arr, N))
