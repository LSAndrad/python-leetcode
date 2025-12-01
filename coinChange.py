def coinChange(coins,amount):

#dp[i] = mínimo de moedas para formar i

    dp = [float('inf')]*(amount+1)  # começo com um valor alto pois vou verificar o mínimo para formar
    dp[0] = 0

    for i in range(1, amount+1): # amount é 4, vetor = [0,1,2,3,4], vai até a posição 5, por isso o dp tem amount + 1
        for coin in coins:
            if coin <= i: # posso usar a moeda
                dp[i] = min(dp[i],dp[i-coin]+1) # Ex com moeda 2: o número de moedas será o número de moedas para formar 0 para 1 moeda, ou seja, apenas 1 moeda.
    
    return dp[amount] if dp[amount] != float('inf') else -1

print(coinChange([1,2,3],10))
