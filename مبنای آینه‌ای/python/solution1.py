# https://quera.ir/problemset/651/

def convert_to_decimal(digits:str,base:str):
    out=0
    base=int(base)
    for index,digit in enumerate(reversed(digits)):
        out+=int(digit)*(base**index)
    return out


def convert_decimal_to_base(digits:str,out_base:str):
    digits = int(digits)
    out_base = int(out_base)
    out = ""
    while digits >out_base:
        out += str(digits%out_base)
        digits = digits // out_base
    out+=str(digits)
    return out[::-1]


# print(convert_to_decimal("505","6"))
# a =convert_decimal_to_base("185","7")
# print(a)


def convert_to_decimal(digits:str,base:str):
    out=0
    base=int(base)
    for index,digit in enumerate(reversed(digits)):
        out+=int(digit)*(base**index)
    return out


def convert_decimal_to_base(digits:str,out_base:str):
    digits = int(digits)
    out_base = int(out_base)
    out = ""
    while digits >out_base:
        out += str(digits%out_base)
        digits = digits // out_base
    out+=str(digits)
    return out[::-1]


# print(convert_to_decimal("505","6"))
# a =convert_decimal_to_base("185","7")
# print(a)


a = input()
b = input()
c = input()


x = str(convert_to_decimal(a,b))
y=convert_decimal_to_base(x,c)

if y == y[::-1]:
    print("YES")
else:
    print("NO")

