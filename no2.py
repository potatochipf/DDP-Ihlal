# No 2
print('ini adalah program sederhana untuk menghitung luas bangun datar')
print('pilih menu angka 1-3 :\n1. Persegi\n2. Lingkaran\n3. Segitiga')
pilihMenu = int(input ("silahkan pilih menu dengan mengetikan angka 1/2/3 :"))
print(pilihMenu)

match pilihMenu:
    case 1:
        print('ini adalah menu untuk menghitung  luas persegi')
        sisi = int(input('silahkan masukan nilai yang mau dihitung :'))
        hitung = sisi*sisi
        print(f'luas persegi adalah : {hitung}')
    
    case 2:
        print('ini adalah menu untuk menghitung  luas lingkaran')
        pi = 3.14
        r = float(input('input jari jari lingkaran:'))
        luas = pi * r * r
        print("Luas lingkaran adalah : "+ str(luas))

    case 3:
        print('ini adalah menu untuk menghitung  luas segitiga')
        L = 1/2
        A = float(input('input alas segitiga:'))
        T = float(input('input tinggi segitiga:'))
        luas = L * A * T
        print("Luas segitiga : "+ str(luas))
    
    case _ :
        print('pilihan tidak valid, silahkan pilih antara 1-3')

    