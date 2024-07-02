

#Solution N1
def rotate_array(array,k):
    if len(array) == 0: return []
    k=k%len(array)
    temp = array[-k:]
    for i in reversed(range(0,len(array)-k)):
        array[i+k]=array[i]
    for i in range(len(temp)):
        array[i]=temp[i]
    return array


print(rotate_array([1,2,3,4,5],3))




#solution N2 
def reverse(array,start,end):
    while(start<end):
        array[start],array[end] = array[end], array[start]
        start +=1
        end -=1
    return array

def rotate_array(array,k):
    if len(array) == 0: return []
    k= k % len(array)
    reverse(array, 0, len(array)-1)
    reverse(array, 0, k-1)
    reverse(array, k, len(array)-1)
    return array

print(rotate_array([1,2,3,4,5],3))









#Soluion N3

def rightRotate(lists, num):
	output_list = []

	
	for item in range(len(lists) - num, len(lists)):
		output_list.append(lists[item])

	
	for item in range(0, len(lists) - num):
		output_list.append(lists[item])

	return output_list



rotate_num = 3
list_1 = [1, 2, 3, 4, 5, 6]

print(rightRotate(list_1, rotate_num))
