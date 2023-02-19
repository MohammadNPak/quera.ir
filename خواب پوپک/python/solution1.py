nums = input().split()
a,b,x= int(nums[0]),int(nums[1]),int(nums[2])

n_a=1
n_b=1
a_list=[]
b_list=[]

while n_a <= a:
    if a%n_a==0:
        a_list.append(n_a)
    n_a+=1
while n_b <= b:
    if b%n_b==0:
        b_list.append(n_b)
    n_b+=1

res=0
for i in a_list:
    for j in b_list:
        if i+j <=x:
            res+=1

print(res)