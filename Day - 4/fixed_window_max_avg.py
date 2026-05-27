# Maximum Average Subarray I

nums = [1,12,-5,-6,50,3]
k=4
window_sum = sum(nums[:k])
max_avg = window_sum/k

for i in range(k, len(nums)):
    window_sum+=nums[i]-nums[i-k]

    max_avg = max(max_avg, window_sum/k)
print(max_avg)
