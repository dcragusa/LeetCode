"""
Demons have captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists
of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight
his way through dungeon to rescue the princess. The knight has an initial health point represented by a positive
integer. If at any point his health point drops to 0 or below, he dies immediately. Some of the rooms are guarded by
demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are
either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive
integers). To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each
step. Return the knight's minimum initial health so that he can rescue the princess. Any room can contain threats or
power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Example 1:
Input: dungeon = [
    [-2,  -3,  3],
    [-5, -10,  1],
    [10,  30, -5]
]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: R->R->D->D.

Example 2:
Input: dungeon = [[0]]
Output: 1
"""

"""
We can solve this in a DP manner, reusing the dungeon array to save space. We work backwards from the end cell to the 
start cell (otherwise we would have to account for multiple possible paths going from start to end). For each cell, we
examine the ones below and to the right of it (if present). We take the maximum of these values and truncate to 0 if
positive - the reason for this being we don't care about positive values, only negative ones getting to the start (in
other words, it's pointless getting 20 health if you lose 30 health on the tile before it - you'll need more than 30
hp to get to the +20hp tile to start with).
Once we have finished iteration, the value in the start cell is the health needed to get to the end. Since we must 
maintain 1hp, the result is 1 minus the start cell value.
"""


def calculate_min_hp(dungeon):
    max_rows = len(dungeon) - 1
    max_cols = len(dungeon[0]) - 1

    dungeon[-1][-1] = min(0, dungeon[-1][-1])

    for row in reversed(range(max_rows)):
        dungeon[row][-1] = min(0, dungeon[row][-1] + dungeon[row+1][-1])

    for col in reversed(range(max_cols)):
        dungeon[-1][col] = min(0, dungeon[-1][col] + dungeon[-1][col+1])

    for row in reversed(range(max_rows)):
        for col in reversed(range(max_cols)):
            value = dungeon[row][col]
            new_value = max(dungeon[row+1][col] + value, dungeon[row][col+1] + value)
            dungeon[row][col] = min(0, new_value)

    return 1 - dungeon[0][0]


assert calculate_min_hp([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]) == 7
assert calculate_min_hp([[0]]) == 1
assert calculate_min_hp([[100]]) == 1
assert calculate_min_hp([[1, -4, 5, -99], [2, -2, -2, -1]]) == 3
assert calculate_min_hp([[1, -3, 3], [0, -2, 0], [-3, -3, -3]]) == 3
