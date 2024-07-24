#Description Problem 
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734952#overview


"""Quicksort is a sorting algorithm based on the divide and conquer approach where
An array is divided into subarrays by selecting a pivot element (element selected from the array).

While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements
greater than pivot are on the right side of the pivot.

The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.

At this point, elements are already sorted. Finally, elements are combined to form a sorted array."""






#Solution N°1:

# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[high]

	# pointer for greater element
	i = low - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# function to perform quicksort


def quickSort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)


#Summary
#The partition function rearranges the elements in the array such that elements less than the pivot are on its left, 
#and elements greater than the pivot are on its right. It also returns the final position of the pivot element.
#Partition Function: Divides the array into elements smaller than the pivot and elements greater than the pivot, placing the pivot in its correct position.
#The quickSort function is the main function that implements the Quicksort algorithm using the partition function. It recursively sorts the elements.
#Quicksort Function: Recursively sorts the left and right subarrays around the pivot.



print("===============================the best Solution===============================")



#Solution N°2:
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Example usage
unsorted_array = [50,2,0,-3,0,1,10]
sorted_array = quicksort(unsorted_array)
print("Sorted Array in Ascending Order:")
print(sorted_array)


