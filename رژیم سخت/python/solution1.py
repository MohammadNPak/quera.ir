# https://quera.org/problemset/20256/


a = input()
red_counter=0
yellow_counter=0
green_counter=0
for color in a :
    if color == "R":
        red_counter +=1
    elif color=="Y":
        yellow_counter +=1
    elif color == "G":
        green_counter+=1

if red_counter >=3:
    output = "nakhor lite"
elif red_counter>=2 and yellow_counter>=2:
    output = "nakhor lite"
elif green_counter==0:
    output = "nakhor lite"
else:
    output = "rahat baash"
print(output)
