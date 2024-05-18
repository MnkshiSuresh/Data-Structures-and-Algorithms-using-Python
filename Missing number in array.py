'''Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

Example 1:

Input:
N = 5
A[] = {1,2,3,5}
Output: 4
Example 2:

Input:
N = 10
A[] = {6,1,2,8,3,4,7,10,5}
Output: 9  '''
-------------------------------------------------------
class Solution:
    def missingNumber(self, arr, N):
        
        for i in range(1,N+1):
            if i not in arr:
                return i
               

if __name__=="__main__":
    arr=[6,3,4,2,1]
    N = len(arr)
    sol = Solution()
    print(sol.missingNumber(arr, N))
