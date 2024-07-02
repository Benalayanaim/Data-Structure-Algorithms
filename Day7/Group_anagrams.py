#Description of the problem 
# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31200350#overview


#Solution N1
def group_anagrams(strings):
    if len(strings) == 0:
        return []
    sorted_string = [''.join(sorted(i)) for i in strings]
    hash = {}
    for i in range(len(sorted_string)):
        if sorted_string[i] in hash:
            hash[sorted_string[i]].append(strings[i])
        else:
            hash[sorted_string[i]] = [strings[i]]

    #we put values here because we worked with key and values in dict and the values his "acv""est" this what they mean 
    return list(hash.values())


print(group_anagrams(["acv","est","set","ess","ses"]))



#Explanation
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33208042#overview







#Solution N2
def groupAnagrams(strs):
    anagrams = {}
    for word in strs:
        # Sort the word to find its base anagram form
        sorted_word = ''.join(sorted(word))
        
        # If this sorted word is not in the dictionary, add it with the current word as the first element of the list
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            # If it is in the dictionary, append the current word to the existing list
            anagrams[sorted_word].append(word)
    
    # Return all the values of the dictionary which are the grouped anagrams
    return list(anagrams.values())

# Example usage:
strs = ["ca", "ac", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

#Explain in directory Explain_anagrams


