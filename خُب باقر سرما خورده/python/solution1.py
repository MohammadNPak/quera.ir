# https://quera.org/problemset/10231/

output = []
for i in range(5):
  line = input()
  if line.find("MOLANA")!=-1 or line.find("HAFEZ")!=-1:
    output.append(i+1)
if len(output):
  print(*output)
else:
  print("NOT FOUND!")