def Coin_Combinations(coins, value):
    """
      A Generalized solution to the coins problem provided by project euler #31
      Read it for more specifications
      coins: a list of coins that can be used
      value: the value that the coins should add to
      returns:
       number of possible combinations to make value with givin coins in "coins"
    """
    maxinput = value
    workspace = [1]+[0]*maxinput
    for coin in coins:
        for place in range(coin,maxinput+1):
            workspace[place] += workspace[place-coin]
            #print workspace
            workspace[0] = 0
    pass
