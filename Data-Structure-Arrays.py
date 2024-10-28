#Arrays are one of the most commonly-used data structures
#The elements of an array are stored in contiguous memory locations
#Arrays are of two types : Static and Dynamic
#Static arrays have fixed, pre-defined amount of memory that they can use, whereas in dynamic arrays this is flexible
#In Python we only have dynamic arrays
#Some basic operations and their complexities are given below :

#Look-up/Accses - O(1)
#Push/Pop - O(1)*
#Insert - O(n)
#Delete - O(n)

array = [5,8,2,9,17,43,25,10]

#Look-up/Acces
#Any element of an array can be accessed by its index.
#We just need to ask for the particular index of the element we are interested in and we will get the element in constant time
first_element = array[0]  #This will return the first element of the array, in this case, 5, in O(1) time
sixth_element = array[5]  #sixth-element = 43 Again, in O(1) time


#Push/Pop
#Push corresponds to pushing or adding an element at the end of the array.
#Similarly, pop corresponds to removing the element at the end of the array.
#Since the index of the end of the array is known, finding it and pushing or popping an element will only require O(1) time
array.append(87) #Adds 87 at the end of the array in O(1) time

#In some special cases, the append(push) operation may take greater time. This is because as mentioned earlier, Python has dynamic arrays
#So when an element is to appended and the array is filled, the entire array has to be copied to a new location
#With more space allocated(generally double the space) this time so that more items can be appended.
#Therefore, some individual operations may reuire O(n) time or greater, but when averaged over a large number of operations,
#The complexity can be safely considered to be O(1)

array.pop() #Pops/removes the element at the end of the array in O(1) time.

print(array)


#Insert
#Insert operation inserts an element at the beginning of the array, or at any location specified.
#This is O(n) operation since after inserting the element at the desired location,
#The elements to the right of the array have to be updated with the correct index as they all have shifted by one place.
#This requires looping through the array. Hence, O(n) time.
array.insert(0,50) #Inserts 50 at the beginning of the array and shifts all other elements one place towards right. O(n)
array.insert(4,0) #inserts '0' at index '4', thus shifting all elements starting from index 4 one place towards right. O(n)

print(array)


#Delete
#Similar to insert, it deletes an element from the specified location in O(n) time
#The elements to the right of the deleted element have to shifted one space left, which requires looping over the entire array
#Hence, O(n) time complexity
array.pop(0) #This pops the first element of the array, shifting the remaining elements of the array one place left. O(n)
print(array)
array.remove(17) #This command removes the first occurence of the element 17 in the array, for which it needs to traverse the entire array, which requires O(n) time
print(array)
del array[2:4] #This command deletes elements from position 2 to position 4, again, in O(n) time
print(array)

///////////////////////////////////////
strings = ['a','b','c','d']
# 4*4 = 16 bytes of storage is used

print(strings[2])

#push  
strings.append('e')      # O(1)
#pop  
strings.pop() 
strings.pop()            # O(1)

#addfirstelement 
strings.insert(0,'x')    #O(n)

#splice
strings.insert(2,'alien')   #O(n)

print(strings)

#Array native python methods :-
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list

#List objects are implemented as arrays. 
#They are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) 
#operations which change both the size and position of the underlying data representation.

#For in depth information on arrays 
#https://docs.python.org/3/tutorial/datastructures.html

#to implement arrays as a stack 
#https://docs.python.org/3/library/collections.html#collections.deque
In Python, lists are implemented as dynamic arrays, and the time complexity for various operations can be described using Big O notation. Here are the common operations and their time complexities:

# <!-- 1. **Indexing (Accessing an element)**
#    - **Operation**: `list[i]`
#    - **Time Complexity**: O(1)

# 2. **Appending an element**
#    - **Operation**: `list.append(x)`
#    - **Time Complexity**: Amortized O(1)

# 3. **Inserting an element at the end**
#    - **Operation**: `list.insert(len(list), x)`
#    - **Time Complexity**: O(1)

# 4. **Inserting an element at the beginning or middle**
#    - **Operation**: `list.insert(i, x)`
#    - **Time Complexity**: O(n)

# 5. **Deleting an element by index**
#    - **Operation**: `del list[i]`
#    - **Time Complexity**: O(n)

# 6. **Removing an element by value**
#    - **Operation**: `list.remove(x)`
#    - **Time Complexity**: O(n)

# 7. **Popping an element from the end**
#    - **Operation**: `list.pop()`
#    - **Time Complexity**: O(1)

# 8. **Popping an element from the beginning or middle**
#    - **Operation**: `list.pop(i)`
#    - **Time Complexity**: O(n)

# 9. **Concatenation**
#    - **Operation**: `list1 + list2`
#    - **Time Complexity**: O(n + m) where n and m are the lengths of the lists

# 10. **Slicing**
#     - **Operation**: `list[start:end]`
#     - **Time Complexity**: O(k) where k is the length of the slice

# 11. **Checking if an element exists**
#     - **Operation**: `x in list`
#     - **Time Complexity**: O(n)

# 12. **Length of the list**
#     - **Operation**: `len(list)`
#     - **Time Complexity**: O(1)

# 13. **Sorting the list**
#     - **Operation**: `list.sort()`
#     - **Time Complexity**: O(n log n)

# 14. **Reversing the list**
#     - **Operation**: `list.reverse()`
#     - **Time Complexity**: O(n)

# ### Summary
# - **O(1)**: Indexing, appending, popping from the end, checking length.
# - **O(n)**: Inserting/removing elements (not at the end), deleting by index, removing by value, checking if an element exists, reversing.
# - **O(n log n)**: Sorting.
# - **O(n + m)**: Concatenation.
# - **O(k)**: Slicing. -->
