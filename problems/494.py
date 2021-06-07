vowels = "AEIOUY"
text = input()
c = 0
for i in text:
    if i in vowels: c += 1
print(c)
