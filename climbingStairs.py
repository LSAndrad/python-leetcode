# para chegar no degrau N
# veio do degrau N-1 ou do degrau N-2

def climbingStairs(n):

    if n<=2:
        return n
    
    previous1 = 1
    previous2 = 2

    for i in range(3,n+1): # n = número de degraus. n+1 porque range não é inclusivo no final
        current = previous1 + previous2
        previous2 = previous1
        previous1 = current
    return current

print(climbingStairs(4))