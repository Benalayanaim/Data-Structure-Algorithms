

#Solution N1

def max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        # Calculate the area between the two lines
        area = min(height[left], height[right]) * (right - left)
        # Update max_area if the current area is greater
        max_area = max(max_area, area)
        
        # Move the pointers towards each other
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Example usage:
height = [3, 5, 10, 6, 30]
print(max_area(height))  # Output should be 49





#=================================================================




#Solution N2

def max_area(array):
    max_area = 0
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            area = min(array[i],array[j])*(j-i)
            max_area = max(max_area,area)
    return max_area


print(max_area([3,7,5,6,8,4]))


