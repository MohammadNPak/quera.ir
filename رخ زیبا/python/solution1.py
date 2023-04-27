# https://quera.org/problemset/178905/

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
x4,y4 = map(int,input().split())

def is_beautiful(x,y):
    if x==x3 or x==x4 or y==y3 or y==y4:
        return True
    else:
        return False


if is_beautiful(x1,y1) != is_beautiful(x2,y2):
    print('happy')
else:
    print('unhappy')
