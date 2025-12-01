def houseRobber(houses):

    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    
    prev1 = 0
    prev2 = 0
    for house in houses:
        print('prev1 = ',prev1,'prev2 + house = ',prev2+house)
        temp = max(prev1,prev2+house)
        prev2 = prev1
        print('prev2 = ',prev2)
        prev1 = temp
        print('prev1 = ',prev1)

    return  prev1

print(houseRobber([1,2,3,4]))