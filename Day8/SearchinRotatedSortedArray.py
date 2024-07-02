#Description of the Problem
#https://leetcode.com/problems/search-in-rotated-sorted-array/description/


#Solution N*1:

def find_index(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1

# Example 1
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 2
print(find_index(nums1, target1))  # Output: 4

# Example 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 10
print(find_index(nums2, target2))  # Output: -1







#Solution N*2:
def find_index(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

# Example 1
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(find_index(nums1, target1))  # Output: 4

# Example 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(find_index(nums2, target2))  # Output: -1

#Explanation in the folder






#Description 
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31186620#overview

#Solution N°3
def search_rotated_sorted_array(nums,target):
    left = 0
    right = len(nums)-1
    while (left <=right):
        middle = (left + right)//2
        if nums[middle] == target: return middle
        if nums[left] <= nums[middle]:
            # left part is sorted
            if target >= nums[left] and target < nums[middle] :
                # explore left part
                right = middle -1
            else:
                left = middle +1
        else:
            #right part is sorted
            if target <= nums[right] and target > nums[middle]:
                left = middle +1
            else:
                right = middle -1
    return -1


print(search_rotated_sorted_array([7,8,1,2,3,4,5,6],5))

#Explanation and in the folder another explanation
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33261728#overview

