#Description of the problem
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31186650#overview
#https://leetcode.com/problems/search-a-2d-matrix/description/

#Solution N°1:
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // n][mid % n]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Example usage:
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16,20],
    [23, 30, 34, 60]
]
target = 30
print(searchMatrix(matrix, target))  # Output: True


target = 13
print(searchMatrix(matrix, target))  # Output: False

#Explanation the folder matrix1

print("===============================================")



#Solution N°2:

def search_in_matrix(matrix,target):
    if len(matrix)==0: 
        return False
    columns = len(matrix[0])
    rows = len(matrix)
    #Binary search to identify the relevant row
    top = 0
    bottom = rows-1
    while(top<=bottom):
        middle = (top + bottom)//2
        if target < matrix[middle][0]:
            bottom = middle -1
        elif target > matrix[middle][columns-1]:
            top = middle+1
        else: 
            break
    if top > bottom: 
        return False
    left =0
    right = columns -1
    while(left<=right):
        middle_val = (left+right)//2
        if target == matrix[middle][middle_val]:
            return True
        elif target < matrix[middle][middle_val]: 
            right = middle_val-1
        else:
            left = middle_val+1
    return False
matrix = [[1,2,3,4],[5,6,7,8],[15,16,17,18],[19,20,30,40]]
print(search_in_matrix(matrix,40))



#Explanation the folder matrix2 and in this link
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33307246#overview



print("===============================================")
#problem
#How do I return the index of the target element in a Python array?

aList = [1,3,5,6,8,9,10,12,34,56,78,456]
def recursiveBinarySearch(aList, target, start, end):
    #aList = sorted(aList)

    if end-start+1 <= 0:
        return False
    else:
        midpoint = start + (end - start) // 2
        if aList[midpoint] == target:
            return midpoint
        else:
            if target < aList[midpoint]:
                return recursiveBinarySearch(aList, target, start, midpoint-1)
            else:
                return recursiveBinarySearch(aList ,target, midpoint+1, end)

print(recursiveBinarySearch(aList,10, 0, len(aList)))#0 it's means from which index we start in this array here from index 0 = 1 in thus array//
                                                        #len(aList)==> mean the end of this index is the lenght of this array 

print(recursiveBinarySearch(aList,123, 0, len(aList))) #False ==>#Because he don't have in this arrya a num 123