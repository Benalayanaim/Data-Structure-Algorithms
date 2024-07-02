# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31027058#reviews


#Type ERROR: unsupported operand type(s) for -: 'list' and 'int'

#def monotonic_array(array):
#    if len(array) == 0:
#        return True
#    first = array[0]
#    last = array[len(array-1)] ## Corrected index calculation
#    if first > last :
#        for i in range(len(array)-1):
#            if array[i] < array[i+1]:
#                return False 
#    elif first == last:
#        for i in range(len(array)-1):
#            if array[i] != array[i+1]:
#                return False
#    else :
#        for i in range(len(array)-1):
#            if array[i] > array[i+1]:
#                return False
#    return True
#
#array1= monotonic_array([])
#array2= monotonic_array([1,1,2])
#array3= monotonic_array([2,2,1])
#array4= monotonic_array([1])
#array5= monotonic_array([1,5,3]) 
#array5= monotonic_array([1,5,3]) 
#print(array1) 
#print(array2) 
#print(array3) 
#print(array4) 
#print(array5) 






#solution 
def monotonic_array(array):
    if len(array) == 0:
        return True
    first = array[0]
    last = array[len(array)-1] #like this right 
    if first > last :
        for i in range(len(array)-1):
            if array[i] < array[i+1]:
                return False 
    elif first == last:
        for i in range(len(array)-1):
            if array[i] != array[i+1]:
                return False
    else :
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                return False
    return True

array1= monotonic_array([])
array2= monotonic_array([1,1,2])
array3= monotonic_array([2,2,1])
array4= monotonic_array([1])
array5= monotonic_array([1,5,3]) 
array6= monotonic_array([3,5,-3]) 
print(array1) 
print(array2) 
print(array3) 
print(array4) 
print(array5) 
print(array6) 

#Explanation 

#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/32784240#reviews





def isMonotonic(nums):
    increasing = decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False
            
    return increasing or decreasing

# Test cases
nums1 = [1, 2, 2, 3]
nums2 = [6, 5, 4, 4]
nums3 = [1, 3, 2]
nums4=  [2,1,-2]
nums5=  []
nums6=  [2]
print(isMonotonic(nums1))  
print(isMonotonic(nums2))  
print(isMonotonic(nums3))  
print(isMonotonic(nums4))  
print(isMonotonic(nums5))  
print(isMonotonic(nums6))  









def isMonotonic(nums):
    if len(nums) <= 1:
        return True
    
    increasing = decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False
            
    return increasing or decreasing

# Test cases
nums1 = [1, 2, 2, 3]
nums2 = [6, 5, 4, 4]
nums3 = [1, 3, 2]
nums4 = [2,1-2]
nums5=  []
nums6=  [2]
print(isMonotonic(nums1))  # Output: True
print(isMonotonic(nums2))  # Output: True
print(isMonotonic(nums3))  # Output: False
print(isMonotonic(nums4))  
print(isMonotonic(nums5))  
print(isMonotonic(nums6)) 