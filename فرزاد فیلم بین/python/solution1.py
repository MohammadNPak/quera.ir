n = int(input())
i=0
movie_names=[]
while i <n:
    name = input()
    movie_names.append(name)
    i+=1
for i in movie_names:
    res=""
    ocd_list=[]
    for j in i.split():
        ocd_list.append(j.capitalize())
    res=" ".join(ocd_list)
    print(res)