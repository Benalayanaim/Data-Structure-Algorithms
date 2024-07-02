# Description of the problem 
#https://leetcode.com/problems/binary-search/description/
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31186602#overview

#Solution N°1:
def binary_search_recursive(nums,target):
    def helper(nums,target,left,right):
        if left>right:
            return -1
        middle = (left + right)//2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            return helper(nums,target,middle+1,right)
        else:
            return helper(nums,target,left,middle-1)
    return helper(nums,target,0,len(nums)-1)


print(binary_search_recursive([10,20,30,40,50,60,66,90,100],66))

#looking here if we put 9 the output is -1 because in this program we write 
#if left>right:return -1
#so this why we -1
print(binary_search_recursive([10,20,30,40,50,60,66,9,100],9))

#so they will return -1 if we don't find the number or if this condition trriger.
#Explanation
# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33261726#overview


#Solution N°2:

def binary_search_iterative(array,target):
    left = 0
    right = len(array)-1
    while left <=right :
        middle = (left + right)//2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

print(binary_search_iterative([2,3,7,9,11,23,37,81,87,89],89))

#Explanation :
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33261722#overview



#Easy solutionN°3:
def search(nums: list[int], target: int) -> int:
    for i , l in enumerate(nums):
        if target == l:
            return i
    return -1

print(search([1,2,3,4,5,6],2))

#just undrestand this line "for i , l in enumerate(nums):"
#with chat 
