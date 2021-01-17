s1 = '''
Game
Roll dices, a dice can roll values from 1 to 6
We are going to roll multiple dices, and we need to roll all
Sum value of rolled dices, the total will be the score

2 dices/rolls
1 1 = 2 
There's 1 way to get a score of 2 with 2 dices

1 2 = 3
2 1 = 3
There are 2 ways to get a score of 3 with 2 dices

1 1 2 = 4
1 2 1 = 4
2 1 1 = 4
There are 3 ways to get a score of 4 with 3 dices

Obj) f of rolls/dices, score, nr_faces_in_dice 
 f (2, 2, 6)
 f (2, 3, 6)
 f (3, 4, 6)

'''

s = '''

Game 
Score 0
To get points you can make diff moves, for example, (2 3 7)

2, 2 => 4
========= There is 1 way of scoring 4 with a set of (2 3 7)

2, 3 => 5
3, 2 => 5
========= There are 2 ways of scoring 5 ...

2 2 3 => 7
2 3 2 => 7
3 2 2
    7 
========= There are 4 ways of scoring 7 ...

Obj) write a f that computes the nr of ways based on a score and move set

nr_of_games (score, move_set) ==> total nr of games


'''


def nr_of_games(score, move_set):
    dp = [0] * (score + 1)
    for current_score in range(score + 1):
        for move in move_set:
            if current_score == move:
                dp[current_score] += 1
            elif current_score > move:
                dp[current_score] += dp[current_score - move]
    print(dp)
    return dp[-1]


# print(nr_of_games(7, [2,3,7]))

def sum_dice_rolls(rolls, score, nr_faces_in_dice):
    mem = {}

    def _sum(cur_rolls, cur_score):
        if cur_score < 0 or cur_rolls < 0 or cur_rolls > cur_score:
            return 0
        if cur_rolls == cur_score:
            return 1
        key = '{}:{}'.format(cur_score, cur_rolls)
        if mem.get(key, None) is not None:
            return mem[key]
        result = 0
        for idx in range(1, min(cur_score, nr_faces_in_dice) + 1):
            result += _sum(cur_rolls - 1, cur_score - idx)
        mem[key] = result
        return result

    result = _sum(rolls, score)
    return result


print('Problem 2 = ')
print(sum_dice_rolls(2, 2, 6))
print(sum_dice_rolls(2, 3, 6))
print(sum_dice_rolls(3, 4, 6))
















