# https://quera.org/problemset/52542/
num=input()
listtest1=list(input().split())
for i in listtest1:
    if int(i)<=3:
        print(int(i)*"*")
    else:
        print("*")