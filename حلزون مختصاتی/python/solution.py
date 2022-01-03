# حلزون مختصاتی
# https://quera.ir/problemset/597/

n = int(input())
counter = 1
prior_pos = []
current_pos = [0, 0]
if n == 1:
    print(0, 0)
else:
    while counter < n:
        if current_pos[0] > 0 and current_pos[1] < 0:
            # prior_pos = current_pos.copy()
            current_pos[1] = -current_pos[1] + 1
        elif current_pos[0] > 0 and current_pos[1] > 0:
            # prior_pos = current_pos.copy()
            current_pos[0] = -current_pos[0]
        elif current_pos[0] < 0 and current_pos[1] > 0:
            # prior_pos = current_pos.copy()
            current_pos[1] = -current_pos[1]
        elif current_pos[0] < 0 and current_pos[1] < 0:
            # prior_pos = current_pos.copy()
            current_pos[0] = -current_pos[0] + 1
        elif current_pos[0] == 0 and current_pos[1] == 0:
            current_pos[0] = 1
            current_pos[1] = 0
        elif current_pos[0] == 1 and current_pos[1] == 0:
            current_pos[0] = 1
            current_pos[1] = 1
        counter += 1
print(current_pos[0], current_pos[1])
