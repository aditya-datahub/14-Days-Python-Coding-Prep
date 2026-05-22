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
print("Number of words: ", len(words))