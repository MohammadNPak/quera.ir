# https://quera.org/problemset/20256/



a = input()
red_counter=a.count("R")
yellow_counter=a.count("Y")
green_counter=a.count("G")

if (red_counter >=3) or (red_counter>=2 and yellow_counter>=2) or (green_counter==0):
    print("nakhor lite")
else:
    print("rahat baash")