#Description of problem
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31343790#overview
#https://leetcode.com/problems/find-the-duplicate-number/description/


#Solution N°1:
def dup_num(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return lst[i]

print(dup_num([1, 2, 2, 4, 5, 10]))

#Explanation
"""
Changes Made:
Parameter Name: Changed the parameter name from list to lst to avoid overwriting the built-in list type.
Equality Check: Corrected the if statement to use == instead of =.
Loop Adjustments: Adjusted the inner loop to start from i + 1 to avoid comparing the same element with itsel
"""





print("=======================================================")







#Solution N°2:
def getDuplicate(nums):
    hare = 0
    tortoise = 0

    while True:
        hare = nums[nums[hare]]
        tortoise = nums[tortoise]


        if hare == tortoise:
            pointer = 0
            while pointer != tortoise:
                pointer = nums[pointer]
                tortoise = nums[tortoise]
            return pointer

print(getDuplicate([1, 2, 2, 4, 6, 10]))


#Explanation in the folderDupSol2




print("=======================================================")









#solutuion N°3:
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

s =Solution()
test = s.findDuplicate([1, 2, 2, 4, 6, 10])
print(test)



#Explanation in the folderDupSol3