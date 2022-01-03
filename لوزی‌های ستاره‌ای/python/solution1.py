# لوزی‌های ستاره‌ای
# https://quera.ir/problemset/9773/

n = int(input())


# n = 1
# **

# n = 3

#  *  *
# ******
#  *  *

# n = 5

#   *    *       *=> 2*i+1   " " => (n - (2*i+1))/2
#  ***  ***
# **********
#  ***  ***
#   *    *
if n == 1:
    print("**")
else:
    for i in range(n):
        if i < n/2:
            star_counter = 2*i+1
            space_counter = (n - (2*i+1))//2
            row = space_counter*" "+star_counter*"*"+space_counter*" "
            row = row*2
            print(row)
        else:
            space_counter = i - int(n/2)
            star_counter = n - space_counter*2
            row = space_counter*" "+star_counter*"*"+space_counter*" "
            row = row*2
            print(row)
