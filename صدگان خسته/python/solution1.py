# https://quera.org/problemset/3406/

a =input()
b =input()

if a==b:
  print(f"{a} = {b}")
else:
  if int(a[::-1])<int(b[::-1]):
    print(f"{a} < {b}")
  else:
    print(f"{b} < {a}")

