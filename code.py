
# Online Python - IDE, Editor, Compiler, Interpreter
import heapq
import copy

def solve(b):
    a = copy.deepcopy(b)
    heapq.heapify(a)
    result = 0
    prev = 0
    curr = 0
    while a:
        m = a[0]
        curr = curr + (m - 1- prev) * len(a) 
        for i, x in enumerate(b):
            if x < m:
                continue 
            curr +=1
            if x == m : 
                result += curr 
                prev = heapq.heappop(a)
            
            
            
            
    return result
        
    
    

print(solve([3,1,2]))
print(solve([7,7,7]))
print(solve([8,5,2,4]))
