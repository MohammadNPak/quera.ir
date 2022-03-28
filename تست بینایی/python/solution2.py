# https://quera.org/problemset/2659/


_ = input()

a = input()
b = input()
counter = 0
for x,y  in zip(a,b):
    if x!=y:
        counter+=1
print(counter)
