# https://quera.ir/problemset/649/


# i = 0

# while i <10:
#     print(i)
#     i+=1
#     # if i ==7:
#     #     break
# else:
#     print("not break")

# print("end of code")


# a = int(input())

# i=2
# while i<a:
#     if a%i==0:
#         print("add morakab")
#         break
#     i+=1
# else:
#     print("addad aval")


# b = int(input())
# j=2
# while j < b:
#     a = j
#     i=2
#     while i<a:
#         if a%i==0:
#             # print("add morakab")
#             break
#         i+=1
#     else:
#         print(a)
#     j+=1


# def is_prime(number):
#     i=2
#     while i<number:
#         if number%i==0:
#             return False
#         i+=1
#     else:
#         return True


# b = int(input())
# j=2
# while j < b:
#     if is_prime(j):
#         print(j)
#     j+=1


def is_prime(number):
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    else:
        return True


output = ""
a = int(input())
b = int(input())
j = a+1
while j < b:
    if is_prime(j):
        output += str(j)+","

    j += 1

print(output[:-1])
