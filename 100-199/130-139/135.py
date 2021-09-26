"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
-Each child must have at least one candy.
-Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1, 0, 2],  Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1, 2, 2],  Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""

"""
This is fairly simple - all we have to do set up an initial candies array filled with 1s (as each child gets at least
one candy). Then we go along this array going right, checking to see if the rating of the current child is greater
than the previous child. If so, we must give the child one more candy than the previous child. We repeat the procedure
going left to catch any increases we missed going right. The result is the sum of the candies array after these passes.
"""


def candy(ratings):
    len_ratings = len(ratings)
    candies = [1] * len_ratings

    for idx in range(1, len_ratings):
        if ratings[idx] > ratings[idx-1]:
            candies[idx] = candies[idx-1] + 1

    for idx in reversed(range(len_ratings-1)):
        if ratings[idx] > ratings[idx+1] and candies[idx] <= candies[idx+1]:
            candies[idx] = candies[idx+1] + 1

    return sum(candies)


assert candy([1, 0, 2]) == 5
assert candy([1, 2, 2]) == 4
assert candy([1, 2, 2, 1]) == 6
assert candy([1, 2, 3, 3, 4, 1]) == 10
