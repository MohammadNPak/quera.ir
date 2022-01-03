# https://quera.ir/problemset/594/

# from mabnay_ayenei import convert_decimal_to_base


def convert_decimal_to_base(digits:str,out_base:str):
    digits = int(digits)
    out_base = int(out_base)
    out = ""
    while digits >out_base:
        out += str(digits%out_base)
        digits = digits // out_base
    out+=str(digits)
    return out[::-1]

a,b =input().split()
# b = input()

x = convert_decimal_to_base(a,b)

sum1 = 0
for i in x[::2]:
    sum1+=int(i)

sum2=0
for i in x[1::2]:
    sum2+=int(i)

if sum1 == sum2:
    print("Yes")
else:
    print("No")