#Description of the problem 
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734970#overview
"""what is the program and how it workd 
https://www.w3schools.com/dsa/dsa_algo_radixsort.php"""


#Solution N°1:
def counting_sort(arr, exp):
    n = len(arr)
    
    # Output array to store sorted numbers
    output = [0] * n
    count = [0] * 10  # Count array to store the count of occurrences of digits (0-9)

    # Store the count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr now contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Apply counting sort to sort elements based on place value.
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage
data = [170, 45, 75, 90, 802, 24, 2, 66]
print("Unsorted Array")
print(data)

radix_sort(data)

print("Sorted Array in Ascending Order")
print(data)



#Explanation in the folder RadixSol1
#after i see the explanation i can use compiler python to see how the problem work to solve 




print("=======================================================")

#Solution N°2:

def radix_sort(array):
    if len(array) == 0:
        return 'empty array'
 
    # Finding the max and the number of digits takes O(n)
    greatest_number = max(array)
    number_of_digits = len(str(greatest_number))
 
    # number of times counting sort needs to be done = digits in greatest number
    # For each digit, perform counting sort. This gives us O(d*(n+k))
    # where d is the number of digits, n is the number of elements, and k is the base (10 for decimal)
    for i in range(number_of_digits):
        counting_sort(array, i)
 
    return array
 
def counting_sort(array, place):
    output = [0] * len(array)
    temp = [0] * 10  # We're using base 10
    digit_place = 10 ** place
 
    # Counting occurrence of digits. This is O(n)
    for num in array:
        digit = (num // digit_place) % 10
        temp[digit] += 1
 
    # Calculate cumulative count. This is O(k), k is base here i.e., 10
    for i in range(1, 10):
        temp[i] += temp[i - 1]
 
    # Populate the output array. This is O(n)
    for j in range(len(array) - 1, -1, -1):
        curr_digit = (array[j] // digit_place) % 10
        temp[curr_digit] -= 1
        insert_position = temp[curr_digit]
        output[insert_position] = array[j]
 
    array[:] = output[:]

# Example usage
data = [170, 45, 75, 90, 802, 24, 2, 66]
print("Unsorted Array:")
print(data)

sorted_data = radix_sort(data)

print("Sorted Array in Ascending Order:")
print(sorted_data)

#the Explantion in the folder RadicSol2