from current import Stack


def reMC(coins,change,minCoins):
    for cents in range(change+1):
        coinCount=cents
        for i in [c for c in coins if c<=cents]:
            if minCoins[cents-i]+1<coinCount:
                coinCount=minCoins[cents-i]+1
        minCoins[cents]=coinCount
    return minCoins
