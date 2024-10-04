N, K = map(int, input().split()) #N banyak jenis buah, K nominal duid
hargabuah = list(map(int,input().split()))
jumlahbuah = []
for i in range(N):
    if hargabuah[i] <=K:
        jumlahbuah.append(i+1)
         
totalbuah=len(jumlahbuah)
print(totalbuah)