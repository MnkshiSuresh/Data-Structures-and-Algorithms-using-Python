'''Given an array Arr consisting of N distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.
 
Example 1:

Input:        
N = 4   
arr[] = {1, 5, 3, 2}      
Output: 2     
Explanation: There are 2 triplets:     
 1 + 2 = 3 and 3 +2 = 5 '''

----------------------------------

class Solution:
    def countTriplet(self, arr, n):
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] in arr:
                    count += 1
        return count

# Driver code
if __name__ == "__main__":
    arr = [1, 5, 3, 2]
    n = len(arr)
    sol = Solution()
    print(sol.countTriplet(arr, n))
