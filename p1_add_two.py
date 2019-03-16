def two_sum(nums, target):
    for k1, v1 in enumerate(nums):
        for k2, v2 in enumerate(nums):
            if v1 + v2 == target and k1 != k2:
                return [k1, k2]


print(two_sum([3, 2, 4], 6))
