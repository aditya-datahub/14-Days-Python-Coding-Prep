nums= [1,4,7,9,2]
print(nums)

nums= [1,0,4,4,7,9,5,7,2]
print("Unique Numbers: ", list(set(nums)))

nums= [1,4,7,9,2]
print("Ascending sorting:" ,sorted(nums))
nums.sort(reverse=True)
print("Descending sorting: ", nums)

print("Maximum: ", max(nums))
print("Minimum: ", min(nums))

print("Sum: ", sum(nums))