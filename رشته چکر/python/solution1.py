# https://quera.org/problemset/106795/
first_input = input().lower()
second_input = input().lower()

if first_input[0] == second_input[-1]:
    print("YES")
else:
    print("NO")
