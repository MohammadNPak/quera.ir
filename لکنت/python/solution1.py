str1=input()
en=1
for i in str1:
    if i=='T':
        en*=2
    if i=='D':
        en*=2
    if i=='F':
        en*=2
    if i=='L':
        en*=2
print(en)