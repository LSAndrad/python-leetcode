from collections import deque

def slidingWindowMaximum(nums, k):
    result = []
    dq = deque()  # Guarda ÍNDICES
    
    for i in range(len(nums)):

        #1. Remove índices fora da janela.
        if dq and dq[0]<i-k+1: #  i = 7, k = 3 => x = 5 (7-3+1) [5,6,7] =
            dq.popleft()
        while dq and nums[dq[-1]]<nums[i]:
            dq.pop()      


        dq.append(i)  # Por enquanto, só adiciona

        if i >= k-1: # k = 3. i >=2, 3 elementos
            result.append(nums[dq[0]])
    return result

# Teste
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(slidingWindowMaximum(nums, k))