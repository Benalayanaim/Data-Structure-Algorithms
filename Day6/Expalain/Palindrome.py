#Descrition of program
# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734780#overview


#///Noticed : In Python Strings are immutable ///


#Solution N:1
def is_palindrom(str):
    new_str = ''
    for i in reversed(range(len(str))):
        new_str += str[i]
    if str == new_str:
        return True
    return False 

print(is_palindrom("SAs"))


#Explain
# https://udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33207836#overview






#Solution N:2
def is_palindrom2(str):
    new_array = []
    for i in reversed(range(len(str))):
        new_array.append(str[i])

    if(''.join(new_array) == str):
        return True
    return False

print(is_palindrom2('aabaa'))


#Explain
# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33207838#overview







#Solution N:3
def is_palindrom3(str):
    i = 0
    j = len(str)-1
    while i<j:
        if str[i] != str[j]:
            return False
        
        i += 1
        j -= 1
    return True

print(is_palindrom3("a"))
    


#Explain
# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33207840#overview








#just in this solution i modified he accept A or a just for take more infomation and experience how handle program 
#and i make some update he accept even the uppercase word and return lower reaed the code you will undrestand what i mean 
#Solution N:4
class Palindrome:
    def check_palindrome(self, word):
        # Convert the word to lowercase to ignore case sensitivity
        word = word.lower()
        # Remove any non-alphanumeric characters
        word = ''.join(char for char in word if char.isalnum())
        # Check if the word is equal to its reverse
        return word == word[::-1] and len(word) > 1

# Example usage
palindrome_checker = Palindrome()
print(palindrome_checker.check_palindrome("libil")) 
print(palindrome_checker.check_palindrome("hhh"))  
print(palindrome_checker.check_palindrome("h"))    
print(palindrome_checker.check_palindrome("aA"))    
print(palindrome_checker.check_palindrome("ad?a")) 


#Explain in file Explain_two