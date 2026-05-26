# Reverse Array Using Two Pointers
nums = [1, 2, 3, 4, 5]

left = 0
right =len(nums)-1

while left<right:
     nums[left], nums[right]= nums[right], nums[left]
     left+=1
     right-=1
print(nums)

