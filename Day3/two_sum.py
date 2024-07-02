#descriptif Problem 
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30413422#reviews




#Solution N1

def two_summ(array,target):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]+array[j] == target:
                return [i, j]
            
    return []

array1 = [1,2,3,4,5]
target11 = 3

print(two_summ(array1,target11))

print(two_summ([1,7,-3,5], 2))

#Explain 
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33191020#reviews








#=========================================================





#Solution N2

def two_sum_optimal(array, target):
    num_available ={}

    for i in range(len(array)):
        needed_val = target - array[i]

        if needed_val in num_available:
            return[i,num_available[needed_val]]
        else:
            num_available[array[i]]=i
        
    return []


arrayy = [2, 5, -1, 3]
TR = 4
print(two_sum_optimal(arrayy, TR))

#Expalin 
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33191024#reviews





#=========================================================









#Solution N3

def two_sum(nums, target):
    # Create a dictionary to store the indices of elements
    num_indices = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement required to reach the target
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_indices:
            # If found, return the indices of current element and its complement
            return [num_indices[complement], i]
        
        # Otherwise, store the index of the current element
        num_indices[num] = i
    
    # If no solution is found, return None OR []
    return []

# Example usage:
nums1 = [2, 7, -11, 15]
target1 = 9
print(two_sum(nums1, target1))  

nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))  

nums3 = []
target3 = 6
print(two_sum(nums3, target3))  
#Explain in the other File


