matriks1 = []
matriks2 = []

print("Masukkan elemen untuk matriks pertama")
for i in range(2):
    baris = []
    for j in range(2):
        nilai = int(input(f"Masukkan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks1.append(baris) 
    
print("\nMasukkan elemen untuk matriks kedua:")
for i in range(2):
    baris = []
    for j in range(2):
        nilai = int(input(f"Masukkan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks2.append(baris)
    
hasil = []
for i in range(2):
    baris = []
    for j in range(2):
        baris.append(matriks1[i][j]+matriks2[i][j])
    hasil.append(baris)
    
print("\nHasil Perjumlahan Matriks:")
for baris in hasil:
    print(baris)