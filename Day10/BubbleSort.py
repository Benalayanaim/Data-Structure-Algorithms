#Description  Problem for BUBBLE Sort Algorithms.
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734928#overview

'About BUBBLE Sort Algorithms.'
#Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. 






#Solution N°1:
def bubble_sort(elements):
  """Sorts a list of elements in ascending order using bubble sort algorithm

  Args:
    elements: The list of elements to be sorted.

  Returns:
    None. The function sorts the elements in-place.
  """
  # Outer loop to iterate through the list n times
  for n in range(len(elements) - 1, 0, -1):
    swapped = False
    # Inner loop to compare adjacent elements
    for i in range(n):
      if elements[i] > elements[i + 1]:
        # Swap elements if they are in the wrong order
        swapped = True
        elements[i], elements[i + 1] = elements[i + 1], elements[i]
    # If we didn't make any swaps in a pass, the list is already sorted and we can exit the outer loop
    if not swapped:
      return

# Sample list to be sorted
elements = [39, 12, 18, 85, 72, 10, 2, 18]
#elements = [1,2,3,4,5,6,87,86]


print("Unsorted list is:")
print(elements)

bubble_sort(elements)

print("Sorted list is:")
print(elements)


#Explanation in the folder Bubble




print("================================================================")



#Solution N°2:
def bubble_sort(array):
  sorted =False
  counter = 0 
  while not sorted:
    sorted = True
    for i in range(len(array)-1-counter):
      if array[i]>array[i+1]:
        array[i],array[i+1]=array[i+1],array[i]
        sorted = False
    
    counter +=1
  return array

print(bubble_sort([2,1,4,3,0]))

#Explanation
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33408298#overview
























