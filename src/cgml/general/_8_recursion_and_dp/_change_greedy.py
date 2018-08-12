def change_greedy(target,denoms):
    change = []
    while target > 0:
        coin = max([d for d in denoms if d <= target])
        change.append(coin)
        target -= coin
    return change


assert change_greedy(40,[25,10,5,1]) == [25,10,5]
assert change_greedy(40,[50,25,20,10,5,1]) == [25,10,5]