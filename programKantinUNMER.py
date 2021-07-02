# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:40:13 2021

@author: yulia  widya 2e 
"""

print("========================================")
print("========KANTIN FAKULTAS TEKNIK UNMER==========")

pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

total1=0
jenis1=""
porsi=0
gelas=0

def fungsimakanan():
   global total1
   global porsi
   global jenis1
   print ("\n~~~~Menu Makanan~~~~")
   print("1. Nasi Goreng - Rp15000")
   print("2. lontong goreng - Rp14900")
   print("3. bakso goreng - Rp12900")
   print("4. rujak goreng - Rp13000")
   print("5. rujak bakso - Rp15000")
   print("6. rujak bakso pecel - Rp17000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       total1=porsi*15000
       print (porsi," porsi Nasi Goreng Telur = Rp", total1)
       jenis1=("Nasi Goreng")
   elif nomor==2:
       total1=porsi*14900
       print (porsi," porsi lontong goreng = Rp", total1)
       jenis1=("lontong")
   elif nomor==3:
       total1=porsi*12900
       print (porsi,"porsi bakso goreng = Rp", total1)
       jenis1=("bakso")
   elif nomor==4:
       total1=porsi*13000
       print (porsi,"porsi rujak goreng = Rp", total1)
       jenis1=("rujak")
   elif nomor==5:
       total1=porsi*15000
       print (porsi,"porsi rujak bakso = Rp", total1)
       jenis1=("rujak bakso")
   elif nomor==6:
       total1=porsi*17000
       print (porsi,"poris rujak bakso pecel = Rp", total1)
       jenis1=("rujak pecel")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()


fungsimakanan()

total2=0
jenis2=""

def fungsiminuman():
   global total2
   global jenis2
   global gelas
   print("\n~~~~Menu Minuman~~~~")
   print("1. teh dingin/hangat/panas - Rp2500")
   print("2. kopi dingin - Rp5000")
   print("3. kopi panas - Rp6500")
   print("4. coca cola dingin - Rp3500")
   print("5. coca cola panas - Rp5000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       total2=gelas*2500
       print (gelas," Gelas teh dingin/hangat/panas = Rp", total2)
       jenis2=(" Gelas Teh")
   elif nomor==2:
       total2=gelas*5000
       print (gelas, " Gelas kopi dingin = Rp", total2)
       jenis2=("es kopi")
   elif nomor==3:
       total2=gelas*6500
       print (gelas, " Gelas kopi panas = Rp", total2)
       jenis2=("Kopi panas")
   elif nomor==4:
       total2=gelas*3500
       print (gelas, "Gelas coca cola dingin = Rp", total2)
       jenis2=("es coca cola")
   elif nomor==5:
       total2=gelas*5000
       print (gelas, "Gelas coca cola panas = Rp", total2)
       jenis2=("hot coca cola")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()


fungsiminuman()
    
totalsemua=0
totalsemua=total1+total2
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n===========================")
print("======= S T R U K   B E L I =====")
print("===========================")
print (" Nama         :",pembeli)
print (" Beli            :",porsi,jenis1,"-", total1)
print ("                    ",gelas,jenis2,"-", total2)
print (" Tagihan      : Rp.",totalsemua)
print (" Uang          : Rp.",uang)
print (" Kembalian  : Rp.",kembalian)
print("===========================")
print("=======terimakasih atas kunjunganya=======")
print("===========================")

ulang = input(" Ulang program? y/t = ")