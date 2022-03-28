# https://quera.org/problemset/3538/


_ = input()
first_list = input().split()
_ = input()
second_list = input().split()
_ = input()
third_list = input().split()

days_of_week = ["shanbe",
                "1shanbe",
                "2shanbe",
                "3shanbe",
                "4shanbe",
                "5shanbe",
                "jome"]

c = 0
for day in days_of_week:
    if day not in first_list and day not in second_list and day not in third_list:
        c += 1

print(c)
