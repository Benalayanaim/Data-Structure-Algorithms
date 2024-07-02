#descriptif
# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734750?start=15#reviews




#Solution N1:

def power_sum(array,power=1):
    sum = 0
    for i in array:
        if type(i) == list:
            sum += power_sum(i, power+1)
        else:
            sum += i
    return sum**power


print(power_sum([1,2,[3,4],[[2]]]))
print(power_sum([1,2,[[2]]]))


#Explain 
# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33191042#reviews



