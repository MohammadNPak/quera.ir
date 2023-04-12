# https://quera.org/problemset/72878/

inpt = input()
inpt = inpt.split()
t = int(inpt[0]); a = int(inpt[1]); b = int(inpt[2])
ArAr_and_MaaMaa_time = 1

ArAr = 0; MaaMaa = 0

while True:
    if t <= 0:
        break
    else:
        t -= (a + ArAr_and_MaaMaa_time)
        ArAr += 1
    
    if t <= 0:
        break
    else:
        t -= (b + ArAr_and_MaaMaa_time)
        MaaMaa += 1

print(f'{ArAr} {MaaMaa}')