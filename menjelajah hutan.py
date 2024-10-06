r, c, m=map(int,input().split())
hutan = []
pos = [0,0]

for _ in range(r):
    hutan.append(list(map(int,input().split())))

move = input()
emas = hutan[pos[0]][pos[1]]    
valid=True
for gerak in move:
    if gerak == 'R'and pos[1]<c-1:
        emas += 3
        hutan[pos[0]][pos[1]] = 0
        pos[1] += 1
    elif gerak == 'L' and pos[1]>0:
        emas -= 2
        hutan[pos[0]][pos[1]] = 0
        pos[1] -= 1    
    elif gerak == 'U' and pos[0]>0:
        emas += 3
        hutan[pos[0]][pos[1]] = 0
        pos[0] -= 1
    elif gerak == 'D'and pos[0]<r-1:
        emas -= 2
        hutan[pos[0]][pos[1]] = 0
        pos[0] += 1
    else:
        valid=False
        break
    emas += hutan[pos[0]][pos[1]]

if not valid or len(move) != m:
    print(emas)
    print("gerakanmu salah bung!")
else:
    print(f"total emas yang didapat adalah {emas}")