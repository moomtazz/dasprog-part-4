n,r,c=map(int,input().split()) # n=jumlah murid, r=baris, c=kolom
bangku={}

for i in range (n):
    urutan, a, b = map(int,input().split())
    bangku[(a,b)]=urutan

for j in range(1,n+1):
    sebelah=False
    for (a,b), teman in bangku.items():
        if teman==j:
            if(a,b+1) in bangku:
                print(bangku[(a,b+1)])
                sebelah=True
            elif(a,b-1) in bangku:
                print(bangku[(a,b-1)])
                sebelah=True
            break
    if not sebelah:
        print(0) 