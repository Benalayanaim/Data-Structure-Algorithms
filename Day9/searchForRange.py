
#description for this problem
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31186632#overview
#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/



#solution N°1:
def find_left_extreme(array,target,range,left,right):
    #base case
    if left > right: return

    middle = (left + right)//2
    if array[middle] == target:
        if middle == 0: range[0]=0
        elif array[middle -1] == target:
            find_left_extreme(array, target, range, left, middle-1)
        else: range[0] = middle
    elif target < array[middle]:
        find_left_extreme(array, target, range, left, middle-1)
    else:
        find_left_extreme(array, target, range, middle+1, right)

def find_right_extreme(array,target,range,left,right):
    # base case
    if left > right: return

    middle = (left + right) // 2
    if array[middle] == target:
        if middle == len(array)-1: range[1]=middle
        elif array[middle+1] == target:
            find_right_extreme(array, target, range, middle+1, right)
        else: range[1] = middle
    elif target<array[middle]:
        find_right_extreme(array, target, range, left, middle-1)
    else:
        find_right_extreme(array, target, range, middle + 1, right)

def search_for_range(array,target):
    range = [-1,-1]
    find_left_extreme(array,target,range,0,len(array)-1)
    find_right_extreme(array,target,range,0,len(array)-1)
    return range


#Because he want in order decreasing so thats why we put the number in order not randomly
#if we put the number randomly so we will have like output [-1, -1] 
print(search_for_range([1,1,3,6,8,9],8))


#Explanation for this code :
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33301292#overview











#solution N°2:
def find_left_extreme(array,target):
    left = 0
    right = len(array)-1
    while(left<=right):
        middle = (left + right)//2
        if array[middle]==target:
            if middle == 0: return 0
            elif array[middle -1 ] == target:
                right = middle -1
            else: return middle
        elif target< array[middle] : right = middle -1
        else: left = middle +1
    return -1

def find_right_extreme(array,target):
    left = 0
    right = len(array)-1
    while(left<=right):
        middle = (left+right)//2
        if array[middle] == target:
            if middle == len(array)-1 : return middle
            elif array[middle+1] == target:
                left = middle+1
            else: return middle
        elif target<array[middle]: right = middle-1
        else: left = middle+1
    return -1


def search_for_range_iterative(array,target):
    left_extreme = find_left_extreme(array,target)
    right_extreme = find_right_extreme(array,target)
    return [left_extreme,right_extreme]



#Because he want in order decreasing so thats why we put the number in order not randomly
#if we put the number randomly so we will have like output [-1, -1] 
print(search_for_range_iterative([1,1,3,4,5,5,6,7,8],5))



#see this example you will undrestand what i say:
print("====================================================")
print(search_for_range_iterative([1,1,3,4,5,6,5,8],5))
#in this case here just we take the elemnet number 4
print("====================================================")
print(search_for_range_iterative([1,1,3,4,5,5,6,7,8],66))
#here because the number not in the list 
print("====================================================")
print(search_for_range_iterative([1,3,4,5,6,5,9,7,8],5))
#Another Example 
print("====================================================")



#Explanation for this code :
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33301294#overview







#solution N°3:
def searchRange(nums, target):
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        first_occurrence = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first_occurrence = mid
                right = mid - 1  # move towards the left (lower indices)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first_occurrence
    
    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        last_occurrence = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                last_occurrence = mid
                left = mid + 1  # move towards the right (higher indices)
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last_occurrence

    first_occurrence = findFirst(nums, target)
    last_occurrence = findLast(nums, target)
    return [first_occurrence, last_occurrence]

# Example usage
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(searchRange(nums1, target1))  # Output: [3, 4]

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(searchRange(nums2, target2))  # Output: [-1, -1]

nums3 = [5, 7, 7, 8, 8, 8, 10]
target3 = 8
print(searchRange(nums3, target3))  # Output: [3, 5]


#Explanation in the folder 





#Solution N4:
def searchRange(nums, target):
    first_occurrence = -1
    last_occurrence = -1
    
    for i in range(len(nums)):
        if nums[i] == target:
            if first_occurrence == -1:
                first_occurrence = i
            last_occurrence = i
    
    return [first_occurrence, last_occurrence]

# Example usage
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(searchRange(nums1, target1))  # Output: [3, 4]

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(searchRange(nums2, target2))  # Output: [-1, -1]

nums3 = [5, 7, 7, 8, 8, 8, 10]
target3 = 8
print(searchRange(nums3, target3))  # Output: [3, 5]



#Explanation in the folder  