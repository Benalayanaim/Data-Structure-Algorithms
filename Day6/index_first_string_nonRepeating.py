#Problem descriptive 
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/30734762#overview





#Soluion N1
def non_repeating_char(str):
    for i in range(len(str)):
        repeat = False
        for j in range(len(str)):
            if i!=j and str[i] == str[j]:
                repeat = True
        if repeat == False:
            return i 
    return None
s = non_repeating_char("1avba")
print(f"Index of the first non-repeating character: {s}" )

#Expalain
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33207830#overview








#Soluion N2

def no_repeating_char(str):
    ht = {}
    for i in str : 
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in range(len(str)):
        if ht[str[i]] == 1:
            return i 
    return None

print(no_repeating_char("abcd"))

#Expalain
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33207832#overview








#Soluion N3

def first_non_repeating_index(string):
    char_count = {}
    index_mapping = {}
    
    # Count occurrences of each character in the string
    for i, char in enumerate(string):
        char_count[char] = char_count.get(char, 0) + 1
        if char not in index_mapping:
            index_mapping[char] = i
    
    # Find the first non-repeating character and return its index
    first_non_repeating_index = None
    for char, count in char_count.items():
        if count == 1:
            if first_non_repeating_index is None or index_mapping[char] < first_non_repeating_index:
                first_non_repeating_index = index_mapping[char]
    
    return first_non_repeating_index

# Test the function
input_string = "abcc"
result_index = first_non_repeating_index(input_string)
print("Index of the first non-repeating character:", result_index)


#Explain 
#in the file named Expalin 