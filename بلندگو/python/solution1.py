# https://quera.org/problemset/3430/
word=input()
print(word)
for i in range(1,len(word)):
  print(word[i]*(i+1) + word[i+1:])