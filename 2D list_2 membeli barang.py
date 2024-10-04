N, M = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))

p_pos= [barang for barang in p if barang>0]
p_neg= [barang for barang in p if barang<0]
c_pos= [uang for uang in c if uang>0]
c_neg= [uang for uang in c if uang<0]

if p_pos and c_neg:
    utang1 = sum(c_neg) - sum(p_pos)
else:
    utang1 = 0  

if p_neg and c_pos:
    utang2 = sum(p_neg) - sum(c_pos)
else:
    utang2 = 0  

if p_pos and c_pos:
    utang3 = min(c_pos) - sum(p_pos)
else:
    utang3 = 0

if p_neg and c_neg:
    utang4 = sum(c_neg) - max(p_neg)
else:
    utang4 = 0

hutang_terbesar = min(utang1, utang2, utang3, utang4)

print(hutang_terbesar) 