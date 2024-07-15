#description of problem
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734940#overview


#Solution N°1:
def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
  
# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)

#explantion in the folder insertSol1



print("=============================================================")



#Solution N°2:
def selection_sort(nums):
    # The outer loop runs n times, where n is the length of the list.
    # This function only uses a constant amount of space to store the indices and temporary values.
    # No additional lists or data structures are created.
    # The outer loop iterates over each element in the list.
    for i in range(len(nums)):
        smallest = i
 
        # The inner loop runs (n - i) times, i is the current iteration of the outer loop.
        # As i increases, the number of times the inner loop runs decreases.
        # The inner loop iterates over the remaining elements in the list after index i.
        for j in range(i+1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
 
        # The swap operation is performed in constant time O(1), 
        # but it's nested in a loop, so in the worst case it could be performed n times.
        # However, since it's not contributing more than the inner loop, 
        # The swapping of elements occurs in-place, i.e., directly within the input list itself.
        # Therefore, this operation does not require any extra space.
        if i != smallest:
            nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums
print(selection_sort([5,4,10,8,3,2]))