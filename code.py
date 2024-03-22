
# Online Python - IDE, Editor, Compiler, Interpreter
import heapq
import copy

def solve(b):
    a = copy.deepcopy(b)
    heapq.heapify(a)
    result = 0
    prev = 0
    while a:
        m = heapq.heappop(a)
        curr = (m - 1) * len(b) - prev
        heapq.heappush(a, m)
        for i, x in enumerate(b):
            if x < m:
                continue 
            curr +=1
            if x == m : 
                result += curr 
                heapq.heappop(a)
                prev += 1
            print(curr, result, x, prev)
            
            
            
            
    return result
        
    
    

print(solve([3,1,2]))
print(solve([7,7,7]))
print(solve([8,5,2,4]))
