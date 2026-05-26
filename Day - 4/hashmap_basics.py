# Here i am revising the previous questions which i already did 

# Question 1 → Character Frequency
s = "python"
freq={}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
print(freq)


# Question 2 → Word Frequency
sentence = "data python data sql python"
words = sentence.split()
freq={}
for word in words:
    freq[word] = freq.get(word,0)+1
print(freq)


# Question 3 → Find Duplicate Numbers
nums = [1,2,3,1,2,5]
printed = []
for num in nums:
    if nums.count(num) > 1 and num not in printed:
        print(num)
        printed.append(num)

# Question 4 → First Non-Repeating Character
sentence = "aabbccdpe"
for ch in sentence:
    if sentence.count(ch)==1:
        print("First Non-Repeating Character:",ch)
        break
else:
    print("Not Found")


# Question 5 → Most Frequent Word
sentence = "sql python sql data sql python"
words = sentence.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
most_frequent = max(counts, key=counts.get)
print("Most Frequent Word in the sentence:", most_frequent)

