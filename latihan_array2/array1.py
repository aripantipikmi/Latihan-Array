ganjil=[]
genap=[]

for i in range(10):
    angka = int(input(f"Masukkan angka ke-{i+1}:"))
    
    if angka % 2 == 0:
        genap.append(angka)
    else:
        ganjil.append(angka)
        
print(f"Angka genap: {genap}")
print(f"Angka ganjil: {ganjil}")