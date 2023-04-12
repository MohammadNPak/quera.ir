# https://quera.org/problemset/52542/
num=input()
output_list=['*'*i if i<=3 else '*' for i in map(int,input().split())]
print('\n'.join(output_list))