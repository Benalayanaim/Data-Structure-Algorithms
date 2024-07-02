#Descritption of problem 
# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/31045600#overview

#more Expalin in leetcode :  https://leetcode.com/problems/longest-substring-without-repeating-characters/description/







#Solution N1

def max_unique_length(str):
    max_len = 0
    start = 0
    seen = {}

    for i in range(len(str)):
        char = str[i]
        if char in seen :
            start = max(start, seen[char]+1)
        max_len = max(max_len,i-start+1)
        seen[char]=i
    return max_len

print(max_unique_length("aav"))


#Explain
# https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33208040#overview







#Solution N2
class Solution : 
    def lengthOFLongestSubstring(self, s):
        n = len(s)
        maxLength = 0
        charmap = {}
        left = 0


        for right in range(n):
            if s[right] not in charmap or charmap[s[right]] < left:
                charmap[s[right]] = right
                maxLength = max(maxLength, right - left + 1) 
            else:
                left = charmap[s[right]] + 1
                charmap[s[right]] = right

        return maxLength
    
so = Solution()

print(so.lengthOFLongestSubstring("ababacde"))



#Expalin in the file Expalin 

