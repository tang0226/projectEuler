#copied a forum solution
def numberOfWays(n,coins):   
    table = [0] *(n+1)
    table[0] = 1
    for coin in coins:
        for i in range(coin, n+1): 
            table[i] += table[i-coin]            
    return table[n]



print(numberOfWays(100, list(range(1, 100))))