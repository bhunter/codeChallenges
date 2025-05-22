"""
Bob likes to play his game on paper. He writes n integers a1, a2, ..., an.
Each of those integers can be either 0 or 1.
He's allowed to do exactly one move:
he chooses two indices i and j (1 ≤ i ≤ j ≤ n) and flips all values ak for which their positions are in range [i, j]
(that is i ≤ k ≤ j). Flip the value of ak means to apply operation ak = 1 - ak.

The goal of the game is that after exactly one move to obtain the maximum number of ones.

Given a list of 0 or 1. Return the maximal number of 1s that can be obtained after exactly one move.

[1, 0, 0, 1, 0]  = 4
[1, 0, 0, 0, 1, 0, 0, 0] = 7
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] = 18
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] = 22
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0] = 11
"""

from typing import List

myLists = [
    [1, 0, 0, 1, 0]
]


"""
Iterate through all possible segments (using nested loops).
For each segment, calculate the number of 1s after flipping it.
Keep track of the maximum number of 1s found so far.
Return the maximum number of 1s. 
"""
class Solution(object):
    def solve(self,l:List[int])->int:

        # Write your code here
        #largest segment
        ak = 0
        start = 0
        end = 0
        #nested loop
        print(f"s: {l[0:len(l)]}")
        for i in range(0,len(l)-1):
            for j in range(i+1,len(l)+1):
                # print(f"i:{i},j:{j}")
                s = l[i:j]
                #invert the sublist values
                newlist = [1-num for num in s ]
                print(newlist)

                #count the ones
                tmpCount = s.count(1)
                # #count the 0s
                tmp0Count = s.count(0)
                # print(f"i:{i}, j:{j}, s:{s})")

                if s.count(0) > s.count(1):
                    print(f"i:{i}, j:{j}, s:{s})")
                    tmpak = tmp0Count - tmpCount
                    if tmpak > ak:
                        ak = tmpak
                #     print(f"tmp0Count:{tmp0Count}, ak:{ak}, len: {len(s)}")
                #     # print(f"i:{i}, j:{j}, s:{s})")
                # # if tmp0Count > len(s) > ak:
                # #     ak = tmp0Count
                #     start = i
                #     end = j

        print(f"largets 0s count: {ak} start: {start}, end: {end}")


if __name__ == "__main__":
    solution = Solution()
    for l in myLists:
        solution.solve(l)