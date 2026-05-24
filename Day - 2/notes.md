# 📝 Day 2 - Python Notes (Frequency & Strings)

---

## 1️⃣ What is Hashmap?

- Hashmap = Dictionary in Python
- Key-Value pairs store karta hai
- Fast lookup → O(1) time complexity

```python
freq = {'a': 2, 'b': 1}
#        key  value
```

> Real life example: Aadhaar card → Name mapping

---

## 2️⃣ Frequency Counting Logic

Kisi bhi string/list mein har element kitni baar aaya — ye count karna

```python
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
```

- `freq.get(char, 0)` → agar char naya hai toh 0 return karo
- `+ 1` → current occurrence add karo

---

## 3️⃣ Enumerate

Loop mein index aur value dono ek saath milti hai

```python
s = "hello"
for index, char in enumerate(s):
    print(index, char)
# 0 h
# 1 e
# 2 l ...
```

> `range(len(s))` ki zaroorat nahi padti!

---

## 4️⃣ Complement Logic

Two Sum jaisi problems mein use hota hai
- Target se current number subtract karo → complement nikalo
- Complement dictionary mein hai? → answer mil gaya!

```python
nums = [2, 7, 11, 15]
target = 9
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        print(seen[complement], i)  # [0, 1]
    seen[num] = i
```

---

## 5️⃣ Set vs Dictionary

| Feature | Set | Dictionary |
|---|---|---|
| Stores | Only values | Key-Value pairs |
| Duplicate | ❌ No | ❌ Keys no, Values yes |
| Order | Unordered | Ordered (Python 3.7+) |
| Use case | Unique check | Count/map karna |
| Syntax | `{1, 2, 3}` | `{'a': 1}` |

```python
# Set - sirf unique values
s = {1, 2, 2, 3}  # → {1, 2, 3}

# Dictionary - key ke saath value
d = {'a': 1, 'b': 2}
```

---

## 6️⃣ New String Methods

```python
s = "  hello world  "

s.split()         # ['hello', 'world'] → spaces pe tod do
s.strip()         # "hello world" → spaces hatao
s.upper()         # "HELLO WORLD"
s.lower()         # "hello world"
s.count('l')      # 3 → kitni baar aaya
s.replace('l','x')# "hexxo worxd"
s.startswith('h') # True
s.endswith('d')   # True
s.find('o')       # 4 → pehla index
```

---

> 💡 **Revision Tip:** Roz ek baar ye notes padho before coding!