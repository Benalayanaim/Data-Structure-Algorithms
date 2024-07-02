#Discreptif Problem 

#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33191024#reviews


#solution N1

def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False
    s_hash, t_hash = {}, {}
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        if char_s not in s_hash:
            s_hash[char_s] = char_t
        if char_t not in t_hash:
            t_hash[char_t] = char_s
        if s_hash[char_s] != char_t or t_hash[char_t] != char_s:
            return False
    return True

print(isomorphic_strings('acada','bbdbe'))

#lezm metab9in ala edhkee false 
#ken nbadlou haka twali true "aacad""bbdbe"

#Explain
#https://www.udemy.com/course/data-structures-and-algorithms-dsa/learn/lecture/33191028#reviews





#########################################################################






#Solutoin Number2

# this function returns true if str1
# and str2 are isomorphic

def areIsomorphic(str1, str2):
	# initializing a dictionary
	# to store letters from str1 and str2
	# as key value pairs
	charCount = dict()
	# initially setting c to "a"
	c = "a"
	# iterating over str1 and str2
	for i in range(len(str1)):
		# if str1[i] is a key in charCount
		if str1[i] in charCount:
			c = charCount[str1[i]]
			if c != str2[i]:
				return False
		# if str2[i] is not a value in charCount
		elif str2[i] not in charCount.values():
			charCount[str1[i]] = str2[i]
		else:
			return False
	return True


# Driver Code
str1 = "xxcv"
str2 = "aatc"

# Function Call
if (len(str1) == len(str2) and areIsomorphic(str1, str2)):
	print("True")
else:
	print("False")


#Explain in the file"Explain_isomorphic"