"""
# Traditional Division Based
def gcd(a, b):
    while b != 0:
        t = b
        b = a % b 
        a = t  
    return a 
"""

# Recursion Based
def gcd(a, b):
    if (b == 0):
        return a 
    else:
        return gcd(b, a % b)
        
print(gcd(5, 11))
