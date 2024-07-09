#Description Problem Insertion Sort:
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734938#overview
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31222266#overview



#Solution N°1:
def insertion_sort(array):
  for i in range(1,len(array)):
        j = i-1
        temp = array[i]

        while j >= 0 and array[j]>temp:
            array[j+1]=array[j]
            j -=1
        array[j+1]=temp

  return array

print(insertion_sort([5,4,3,2,1]))  


#Explanation 
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33408466#overview



print("================================================================")


#Solution N°2:
def insertion_sort(elements):
  """Sorts a list of elements in ascending order using insertion sort algorithm

  Args:
    elements: The list of elements to be sorted.

  Returns:
    None. The function sorts the elements in-place.
  """
  # Iterate through elements from the second element to the end
  for i in range(1, len(elements)):
    # The current element to be inserted into the sorted portion
    key = elements[i]
    # Initialize j to be the index of the last element of the sorted portion
    j = i - 1
    # Move elements of the sorted portion that are greater than the key to one position ahead
    while j >= 0 and elements[j] > key:
      elements[j + 1] = elements[j]
      j -= 1
    # Insert the key element into its correct position
    elements[j + 1] = key

# Sample list to be sorted
elements = [3,5,2,4,1]

print("Unsorted list is:")
print(elements)

insertion_sort(elements)

print("Sorted list is:")
print(elements)


#Explanation in Folder Insertion