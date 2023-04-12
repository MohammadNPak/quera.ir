# https://quera.org/problemset/2534/
column_number=int(input())
column_height=[]
a=0
while a<column_number:
    b=int(input())
    column_height.append(b)
    a+=1
s=0
for i in column_height:
    s+=i
average=int(s/len(column_height))

i_sum=0
for i in column_height:
    i_count=0
    if i < average:
        while i_count<average-i:
            i_count+=1
    i_sum+=i_count

print(i_sum)