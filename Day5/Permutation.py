#Description Problem

#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31042108#reviews



#Solution N°1

def all_permutations(nums):
    permutations = []
    if len(nums) == 0:
        return [[]]
    
    def helper(nums, i):
        if i == len(nums) - 1:
            permutations.append(nums.copy())
            return
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            helper(nums, i+1)
            nums[i], nums[j] = nums[j], nums[i]

    helper(nums, 0)
    return permutations

array = [1,2,3,4]
print(all_permutations(array))
    

#Explanation 

#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33206176#reviews





#Solution N°2

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start):
            if start == len(nums):
                permutations.append(nums[:])
            else:
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]

        permutations = []
        backtrack(0)
        return permutations
    
array2 =[1,2,3]
s = Solution()
print(s.permute(array2))    


#Explanation 
#https://leetcode.com/problems/permutations/solutions/4853218/beat-98-64-full-explanation-with-pictures





#Solution N°3

#https://leetcode.com/problems/permutations/solutions/3851480/c-python-c-0ms-backtrack-with-graph-explained-beginner-friendly