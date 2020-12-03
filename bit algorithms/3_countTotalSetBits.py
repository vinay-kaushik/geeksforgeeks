# Count total set bits in all numbers from 1 to n

# Given a positive integer n, count the total number of set bits in binary representation of all numbers from 1 to n.
# Examples:

# Input: n = 3
# Output:  4
# explanation: 
# 0 = 0000
# 1 = 0001
# 2 = 0010
# 3=  0011

# Input: n = 6
# Output: 9

# Input: n = 7
# Output: 12

# Input: n = 8
# Output: 13
def countBits(num):
    a=bin(num).split('0b')[1]
    return a.count('1')


def countTotalSetbits(n):
    ans=0
    for i in range(n+1):
        ans+=countBits(i)
    return ans

print(countTotalSetbits(3))

print(countTotalSetbits(8))


