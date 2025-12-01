from collections import deque

def jumpGameII_greedy(nums):

    if len(nums) <= 1:
        return 0
    
    jumps = 0 # número de pulos
    current_end  = 0 # final da janela atual
    farthest= 0 # alcance máximo descoberto

    for i in range(len(nums)-1): # indice i = indice do array
        # qual o mais longe que chego no 0, 1, 2?
        # [1,2,3,4] -> (0,1), (1,3), (3,5)
        farthest = max(farthest, i + nums[i])

        if i == current_end: # i está no zero inicialmente, preciso dar um pulo e jogar o final para o máximo que consigo chegar
            jumps +=1
            current_end = farthest

            if current_end >= len(nums)-1: # n-1 = última posição do vetor.
                break

    return jumps

print(jumpGameII_greedy([1,2,3,4]))