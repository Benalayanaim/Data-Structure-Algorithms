#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734680#reviews

#Brute force method

def sorted_squared(array):
    new_array = [0]*len(array)
    for i in range(len(array)):
        new_array[i] = array[i]**2
        #new_array[i] = array[i]*array[i]
    new_array.sort()
    return new_array

    
print (sorted_squared([8,-5,10]))

#explain the first solution
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/32784230#reviews




#3Solution  
# Time = O(n) Space = O(n)
def sorted_squared(array):
    i = 0
    j = len(array) - 1
    new_array = [0] * len(array)
    for k in reversed(range(len(array))):
        sq_i = array[i]**2
        sq_j = array[j]** 2
        if sq_i > sq_j:
            new_array[k] = sq_i
            i += 1
        else:
            new_array[k] = sq_j
            j -= 1
    return new_array

print (sorted_squared([8,-5,10]))
#Explain the soltuion number two
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/32784232#reviews




#3Solution  
def square_array_sorted(arr):
    """
    Function to square each element of an array and sort it in ascending order.

    Parameters:
        arr (list): Input array.

    Returns:
        list: Array with each element squared and sorted in ascending order.
    """
    squared_arr = [x ** 2 for x in arr]
    squared_arr.sort()
    return squared_arr

# Example usage:
input_array = [8,-5,10]
sorted_squared_array = square_array_sorted(input_array)
print(sorted_squared_array)  # Output: [1, 4, 9, 16, 25]

#or we can do this 
##print(square_array_sorted([5,8,10]))