#Descriptif Problem

#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734726#reviews



#solution Number N°1

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
         
n= 4
print(fibonacci(n))


#Explanation
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33191034#reviews






#solution Number N°2

ht = {0 : 0, 1: 1}

def fibonaccci(n):
    if n in ht :
        return ht [n]
    
    else : 
        ht[n] = fibonaccci(n - 1) + fibonaccci(n - 2)
        return ht[n]

print(fibonaccci(4))

#Explain 

#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33191036#reviews






#solution N°3

def fibonacci_2(n):
    if n <= 1 :
        return 1
    
    prev = 0
    curr = 1 
    counter = 1

    while counter < n :
        next = curr + prev
        counter += 1
        prev = curr
        curr = next

    return curr 

print(fibonacci_2(4))


#Explain 
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33191038#reviews

