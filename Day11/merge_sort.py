#Description Problem
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734942#overview

"""--Merge sort is a popular and efficient sorting algorithm that utilizes the divide and conquer technique of sorting.
--Major disadvantage of merge sort is that it uses additional memory to store the temporary copies of arrays before merging them.
"""


#Solution N°1:

def mergeSort(arr):
    if len(arr) > 1:

        # Create sub_array2 ← A[start..mid] and sub_array2 ← A[mid+1..end]
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        # Sort the two halves
        mergeSort(sub_array1)
        mergeSort(sub_array2)
       
        # Initial values for pointers that we use to keep track of where we are in each array
        i = j = k = 0

    # Until we reach the end of either start or end, pick larger among
    # elements start and end and place them in the correct position in the sorted array
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

    # When all elements are traversed in either arr1 or arr2,
    # pick up the remaining elements and put in sorted array
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1

arr = [10, 9, 2, 4, 6, 13]
mergeSort(arr)
print(arr)

#Solution in the Folder Merge



print("=================================================")


#Solution N°2:
def merge_sorted_arrays(array1, array2):
    merged_array = []
    i, j = 0, 0
    # This loop runs a maximum of min(len(array1), len(array2)) times.
    # This loop runs until we've gone through one of the arrays completely.
    # Since we're building the merged_array from the elements of array1 and array2, 
    # the space complexity of this function will be proportional to the total number of elements in both arrays.
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1
    
    # These loops run a maximum of len(array1) - i and len(array2) - j times, respectively.
    # They will only execute if all elements of the other array have been appended to merged_array.
    # These loops handle the case where one array is exhausted before the other.
    # The remaining elements of the non-exhausted array are then added to the end of the merged array.
    while i < len(array1):
        merged_array.append(array1[i])
        i += 1
    while j < len(array2):
        merged_array.append(array2[j])
        j += 1
 
    return merged_array
 
def merge_sort(array):
    # A single or empty array is already sorted, so return as is.
    # This acts as the base condition for this recursive function.
    # If the array has only one or no element, it doesn't require extra space.
    if len(array) <= 1:
        return array
    
    middle = len(array) // 2
    # In the merge_sort function, the input array is divided into two halves.
    # These halves may not be equal if the original array has an odd length.
    # However, this division does not contribute to the space complexity,
    # as it just creates two new references to the original array.
    left_side = merge_sort(array[:middle])
    right_side = merge_sort(array[middle:])
 
    # Here, merge_sort() is called recursively
    # Because for each recursive call, the array is divided into two halves.
    
    return merge_sorted_arrays(left_side, right_side)

# Example usage of merge_sort function

# Input array
array = [38, 27, 43, 3, 9, 82, 10]

# Call the merge_sort function
sorted_array = merge_sort(array)

# Output the result
print("Input array:", array)
print("Sorted array:", sorted_array)




("==========================#Clear Code=======================")

def merge_sorted_arrays(array1, array2):
    merged_array = []
    i, j = 0, 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1
    while i < len(array1):
        merged_array.append(array1[i])
        i += 1
    while j < len(array2):
        merged_array.append(array2[j])
        j += 1
    return merged_array

def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left_side = merge_sort(array[:middle])
    right_side = merge_sort(array[middle:])
    return merge_sorted_arrays(left_side, right_side)

# Example usage of merge_sort function
array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(array)
print("Input array:", array)
print("Sorted array:", sorted_array)




print("=====================Advanced============================")

#Solution N°3:
"""Sorting Custom Objects Since now we are familiar with the basics of merge sort in python, let us use the same as above for sorting our custom objects, 
which in most cases isn't what we want. A better idea is to make the algorithm itself more versatile, and pass a comparison function to it."""

class Invention:
    def __init__(self, item, person, year):
        self.item = item
        self.person = person
        self.year = year

    def __str__(self):
        return str.format("Item: {}, Person: {}, Year: {}", self.item, self.person, self.year)

def mergeSort(arr, compare):
    if len(arr) > 1:

        # Create sub_array2 ← A[start..mid] and sub_array2 ← A[mid+1..end]
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        # Sort the two halves
        mergeSort(sub_array1, compare)
        mergeSort(sub_array2, compare)

        # Initial values for pointers that we use to keep track of where we are in each array
        i = j = k = 0

    # Until we reach the end of either start or end, pick larger among
    # elements start and end and place them in the correct position in the sorted array
        while i < len(sub_array1) and j < len(sub_array2):
            if compare(sub_array1[i], sub_array2[j]):
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

    # When all elements are traversed in either arr1 or arr2,
    # pick up the remaining elements and put in sorted array
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1

p1 = Invention("Steamboat", "Robert Fulton", 1807)
p2 = Invention("Airplane", "Wright Brothers", 1903)
p3 = Invention("Light Bulb", "Thomas Edison", 1879)
p4 = Invention("Television", "Philo Farnsworth", 1927)

arr = [p1, p2, p3, p4]

mergeSort(arr, lambda prod1, prod2: prod1.year < prod2.year)

print("Products sorted by year:")
for p in arr:
    print(p)

print()

mergeSort(arr, lambda prod1, prod2: prod1.item < prod2.item)
print("Products sorted alphabetically:")
for p in arr:
    print(p)

#Explanation in the folder MergeAdvanced