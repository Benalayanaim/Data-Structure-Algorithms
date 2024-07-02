#Descriptif Problem 
# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31042122#reviews



#Solution N°2:

def power_set(nums):
    output = []
    def helper (nums, i, subset):
        if i == len(nums):
            output.append(subset.copy())
            return
        helper(nums, i+1, subset)
        subset.append(nums[i])
        helper(nums, i+1, subset)
        subset.pop()
    
    helper(nums, 0, [])
    return output

nums = [1,2,3]

print(power_set(nums))


#Explanation
# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33206178#reviews









#Solution N°2:

import copy

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        powerset = [[]]
        for num in nums:
            powersetCopy = copy.deepcopy(powerset)
            powersetCopy.pop(-1)
            for s in powerset:
                s.append(num)
            powerset.extend(powersetCopy)
            powerset.append([])
        return powerset
    
s = Solution()

nums =[2,3]

print(s.subsets(nums))



#Descrition 
# https://leetcode.com/problems/subsets/solutions/4154383/simple-for-loop-no-dfs-easy-to-understand

#Deecopy ?
#https://www.google.com/search?q=deep+copy+in+python&rlz=1C1CHBD_frTN1087TN1087&oq=deecopy+in+&gs_lcrp=EgZjaHJvbWUqCQgBEAAYDRiABDIGCAAQRRg5MgkIARAAGA0YgAQyCAgCEAAYDRgeMggIAxAAGA0YHjIICAQQABgNGB4yCAgFEAAYDRgeMggIBhAAGA0YHjIICAcQABgNGB4yCAgIEAAYDRgeMggICRAAGA0YHtIBCDU1ODRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8