# LeetCode: Two Sum
# Difficulty: Easy

nums = [2,7,11,15]
target = 9

lookup={}

for i, num in enumerate(nums):

    complement = target - num

    if complement in lookup:
        print([lookup[complement], i])
        break
    else:
        lookup[num] = i
