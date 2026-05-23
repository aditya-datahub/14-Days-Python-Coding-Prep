for i in range(1,11):
    print(i)

print("Even Numbers: ")
for i in range(1,21):
    if i % 2 == 0:
        print(i)

print("Odd Numbers: ")
for i in range(1,21):
    if i % 2 != 0:
        print(i)

print("Sum of first 100 numbers: ")
total=0
for i in range (1,101):
    total+=i
print(total)

print("Multiplication table :")
num=5
for i in range(1, 11):
    print(num*i)

print("Elements of Lists: ")
nums = [4,7,2,9]
for num in nums:
    print(num)

nums = [4,7,2,9,1]
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print("Largest number: ", largest)

# Largest in the list
nums= [1,11,6,3,8,0,5,2,7,4]
largest = nums[0]
for num in nums:
    if num>largest:
        largest=num
print("Largest number: ",largest)