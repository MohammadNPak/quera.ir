listtest1,dicttest1=[],{}
for i in range(int(input())):
    listtest1.append(input())
    listtest1[i]=(list(listtest1[i].split()))[0]
for i in listtest1:
    dicttest1[i]=listtest1.count(i)
t=dicttest1[listtest1[0]]
for i in dicttest1.values():
    if i>t:
        t=i
print(t)
        

