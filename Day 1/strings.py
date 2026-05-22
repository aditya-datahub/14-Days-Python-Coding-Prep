s = "data analyst"
print(s[::-1])

s = "data analyst"
count = 0
for char in s:
    if char in 'aeiou':
        count+=1
print("Number of vowels: ", count)


s= "I am damn very rich"
words=s.split()
print(words)
print("Total Number of words in a sentence: ", len(words))


# Count the occurrences of each character in the given word 
s="banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
print(freq)