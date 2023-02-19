name = input()

vowel_list=["a","e","i","o","u"]

r=1

for n in name:
    if n in vowel_list:
        r*=2

print(r)