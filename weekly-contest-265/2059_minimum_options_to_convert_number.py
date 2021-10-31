# 2059. Minimum Operations to Convert Number
# User Accepted:1478
# User Tried:2163
# Total Accepted:1544
# Total Submissions:5238
# Difficulty:Medium
# You are given a 0-indexed integer array nums containing distinct numbers, an integer start, and an integer goal. There is an integer x that is initially set to start, and you want to perform operations on x such that it is converted to goal. You can perform the following operation repeatedly on the number x:
#
# If 0 <= x <= 1000, then for any index i in the array (0 <= i < nums.length), you can set x to any of the following:
#
# x + nums[i]
# x - nums[i]
# x ^ nums[i] (bitwise-XOR)
# Note that you can use each nums[i] any number of times in any order. Operations that set x to be out of the range 0 <= x <= 1000 are valid, but no more operations can be done afterward.
#
# Return the minimum number of operations needed to convert x = start into goal, and -1 if it is not possible.
#
#
#
# Example 1:
#
# Input: nums = [1,3], start = 6, goal = 4
# Output: 2
# Explanation:
# We can go from 6 → 7 → 4 with the following 2 operations.
# - 6 ^ 1 = 7
# - 7 ^ 3 = 4
# Example 2:
#
# Input: nums = [2,4,12], start = 2, goal = 12
# Output: 2
# Explanation:
# We can go from 2 → 14 → 12 with the following 2 operations.
# - 2 + 12 = 14
# - 14 - 2 = 12
# Example 3:
#
# Input: nums = [3,5,7], start = 0, goal = -4
# Output: 2
# Explanation:
# We can go from 0 → 3 → -4 with the following 2 operations.
# - 0 + 3 = 3
# - 3 - 7 = -4
# Note that the last operation sets x out of the range 0 <= x <= 1000, which is valid.
# Example 4:
#
# Input: nums = [2,8,16], start = 0, goal = 1
# Output: -1
# Explanation:
# There is no way to convert 0 into 1.
# Example 5:
#
# Input: nums = [1], start = 0, goal = 3
# Output: 3
# Explanation:
# We can go from 0 → 1 → 2 → 3 with the following 3 operations.
# - 0 + 1 = 1
# - 1 + 1 = 2
# - 2 + 1 = 3
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# -109 <= nums[i], goal <= 109
# 0 <= start <= 1000
# start != goal
# All the integers in nums are distinct.

# Solution:
#
# A typical BFS search problem: https://leetcode.com/contest/weekly-contest-265/problems/minimum-operations-to-convert-number/
# keywords: minimum number of operations from one state to another state, normally can use a tuple, or class Node to store the current level
# sample: https://www.geeksforgeeks.org/minimum-number-operation-required-convert-number-x-y/
# Fast BFS solution: https://leetcode.com/problems/minimum-operations-to-convert-number/discuss/1550126/Python3-Fast-BFS-(~100-200-ms)


import collections
from typing import List

# can also use a tuple or named tuple for this
class Node:
    def __init__(self, val, level):
        self.val = val
        self.level = level

    def __str__(self):
        return f"{self.val}, {self.level}"


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        # BFS search problem
        # numbers visited, so that we don't retry on this numbers
        seen = set()
        q = collections.deque([Node(start, 0)])

        while q:
            item = q.popleft()

            if item.val == goal:
                print(item.level)
                return item.level

            if item.val in seen:
                continue

            if item.val < 0 or item.val > 1000:
                continue

            # if can reach the goal in one more step
            for n in nums:
                q.append(Node(item.val + n, item.level + 1))
                q.append(Node(item.val - n, item.level + 1))
                q.append(Node(item.val ^ n, item.level + 1))

            seen.add(item.val)
        return -1


solution = Solution()
solution.minimumOperations([1, 3], 6, 4)
solution.minimumOperations([2, 8, 16], 0, 1)
solution.minimumOperations(
    [
        274504599,
        -437121852,
        -283671014,
        -795227961,
        504793587,
        -655990799,
        -903306522,
        44919307,
        -873921107,
        435103173,
        -233943318,
        -364255446,
        -559614087,
        -727247460,
        -187800152,
        -228958874,
        373958305,
        637920438,
        235436095,
        -596133383,
        464339218,
        -67824712,
        -155028908,
        168017302,
        361823236,
        195637352,
        -495807030,
        -283876713,
        517899793,
        -562939689,
        884969425,
        -144330241,
        140538827,
        -536479469,
        768251206,
        -640028608,
        806134401,
        243968407,
        928102192,
        -480188410,
        -652340704,
        -862758854,
        137351112,
        648721527,
        249762676,
        624620853,
        -392218813,
        -999179129,
        731919183,
        330383470,
        861417443,
        -679928265,
        -850093860,
        105372736,
        -331113772,
        377702286,
        265400395,
        -511047215,
        492824547,
        118533263,
        802729743,
        91293283,
        -596122218,
        503153602,
        -392161752,
        -536359573,
        469464778,
        -519480260,
        -437818942,
        43191911,
        -325148088,
        914414872,
        -779527485,
        499668349,
        604223142,
        158035493,
        -133335863,
        452500770,
        593642940,
        881994837,
        -393244441,
        -740955862,
        369681444,
        -649744897,
        -329622834,
        -727346152,
        216135938,
        660402034,
        157047130,
        98520751,
        389074028,
        332247407,
        -209362397,
        -405846547,
        -976164396,
        179697702,
        482640852,
        113156802,
        -764726927,
        21196820,
        475924861,
        -501387010,
        -521285998,
        -73340730,
        -341407987,
        -410283280,
        -618814157,
        388062458,
        -52090234,
        -943486285,
        438909665,
        386411224,
        829785577,
        878471402,
        306505406,
        -4019276,
        242674243,
        133684521,
        626711549,
        427600365,
        -907767977,
        -58201536,
        -768231545,
        357227318,
        -830719646,
        608805401,
        -189212199,
        288239474,
        692386759,
        908023931,
        -120320781,
        -239958589,
        680092226,
        207253648,
        274039857,
        157541875,
        216046740,
        577951839,
        345003653,
        -380997882,
        837933318,
        -372547856,
        -593257214,
        -376937702,
        -215397501,
        -490627366,
        397047895,
        171228292,
        239947581,
        574138161,
        133786400,
        -349032470,
        224529998,
        812411777,
        647669892,
        488917,
        -674063913,
        768370921,
        -37596428,
        -656866372,
        367475563,
        4811396,
        -864970305,
        -22343842,
        781134974,
        -320627062,
        -943951001,
        -724118919,
        23519930,
        -372268648,
        714884514,
        -921267107,
        -629610933,
        -210498943,
        629593893,
        -543099666,
        989641699,
        -520568809,
        302398795,
        462461247,
        -493362512,
        -517267543,
        896586688,
        738136629,
        792759663,
        77849471,
        163099930,
        -294652452,
        -586051267,
        138373545,
        -45443242,
        -178006635,
        126656767,
        -370740793,
        -142028216,
        -656478789,
        -909865539,
        -45016267,
        -331506071,
        -875778621,
        -575234905,
        -795010054,
        -217915587,
        28709532,
        410822428,
        -253100539,
        542188248,
        -292261868,
        -628494325,
        -137807006,
        -62295850,
        -960968938,
        651503967,
        -804449486,
        -912908442,
        407895859,
        -312220179,
        -373281077,
        -126441710,
        587251290,
        807148112,
        -542439701,
        -437800095,
        136518757,
        947027117,
        -162031226,
        -883838131,
        -441985931,
        105920835,
        300258318,
        -461749685,
        312341616,
        -722559772,
        553077273,
        100170653,
        -791911093,
        260884109,
        -515528241,
        519874204,
        726741845,
        116213300,
        396117093,
        -646099763,
        896174142,
        484441559,
        170623996,
        731971679,
        -683531213,
        429220971,
        51501373,
        -980518207,
        337856564,
        932447220,
        790777174,
        -164285774,
        184598181,
        542501755,
        -295103903,
        322292600,
        -515696143,
        466063434,
        268858116,
        19617585,
        -668148351,
        595835834,
        -875679692,
        306780299,
        465852737,
        -749476049,
        496973136,
        108307092,
        -62169373,
        -613000035,
        -15802981,
        380806050,
        -15599477,
        224196161,
        -786436446,
        -102721720,
        966016112,
        -449681577,
        -571359760,
        -30870357,
        907947772,
        -397757285,
        -415978672,
        204756474,
        -676646192,
        879829138,
        154543119,
        -37915616,
        353546466,
        121384343,
        679059598,
        -575886433,
        -58814987,
        375756597,
        -737810759,
        -640442425,
        -830225084,
        -131054299,
        -448790015,
        -121208252,
        -182631226,
        -828929325,
        860254702,
        -966027942,
        693239701,
        221755949,
        954184244,
        609025156,
        602818238,
        348029234,
        191806330,
        -776743553,
        217516433,
        625978431,
        146580109,
        -176159863,
        142705862,
        332507932,
        -911208273,
        607714224,
        -487331269,
        -491001799,
        31873551,
        -890999237,
        203866747,
        831181692,
        -474880013,
        -414589485,
        708339893,
        -68899679,
        35636137,
        43747302,
        -970885272,
        301068191,
        175227438,
        906089806,
        -622934104,
        613550487,
        212679441,
        237390198,
        -383871498,
        359829413,
        -18858272,
        -564035296,
        -68723821,
        902159573,
        925503754,
        841238795,
        -550055927,
        -710708273,
        473810306,
        -942061728,
        -630129098,
        473871569,
        -38610927,
        798344511,
        -585307353,
        17981580,
        575350042,
        -708955832,
        438058040,
        -225128624,
        441551583,
        -669250624,
        -904359642,
        67471216,
        836221913,
        377382388,
        986685062,
        614075075,
        -969748019,
        -688247479,
        234834944,
        1,
    ],
    704,
    884969425,
)
