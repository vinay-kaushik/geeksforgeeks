# Find the element that appears once

# Given an array where every element occurs three times, except one element which occurs only once. Find the element that occurs once. Expected time complexity is O(n) and O(1) extra space.
# Examples :

# Input: arr[] = {12, 1, 12, 3, 12, 1, 1, 2, 3, 3}
# Output: 2
# In the given array all element appear three times except 2 which appears once.

# Input: arr[] = {10, 20, 10, 30, 10, 30, 30}
# Output: 20
# In the given array all element appear three times except 20 which appears once.

# dictionary appraoch. Taking count of every and every element and only return the element which appears once
def elementAppearonce_dictionary(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    for i,j in enumerate(d):
        # Taking the count of the elements in the dictioanry and if its 1 then return it
        if d[j]==1:
            return j

# Using the set formula approach
# As the problem statement says that the element appears thrice. 
def elementAppearOnce_SetFormula(arr):
    app=set(arr)
    ans = (3*sum(list(set(arr)))- sum(arr))//2
    return ans


arr=[12, 1, 12, 3, 12, 1, 1, 2, 3, 3]


print( elementAppearonce_dictionary(arr))
print(elementAppearOnce_SetFormula(arr))


