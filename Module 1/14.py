from heapq import nlargest
dict1 = {'a':720, 'b':8764, 'c': 56090,'d':4020, 'e':74, 'f': 520}  
three_largest = nlargest(3, dict1, key=dict1.get)
print(three_largest) 
