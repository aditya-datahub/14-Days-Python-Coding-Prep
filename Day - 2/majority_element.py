nums = [2,2,1,1,1,2,2]
freq = {}

for num in nums:
    freq[num] = freq.get(num,0)+1
print(freq)

for key, value in freq.items():
    if value > len(nums)/2:
        print("Majority Element:",key)

