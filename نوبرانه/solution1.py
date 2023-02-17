
ghermezi=0
darsad=input().split()
for i in darsad :
    if int(i)>=80 :
        ghermezi+=1

if ghermezi>=3 :
    print("Mamma mia!")

elif ghermezi==1 or ghermezi==2 :
    print ("Mamma mia!!")

else :
    print ("Mamma mia!!!")
