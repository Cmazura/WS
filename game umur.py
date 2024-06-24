#----------------------------
# MENENTUKAN UMUR PENCEN ANDA BAGI KAKITANGAN KERAJAAN
#----------------------------
import time
print("----------------------------")
print(time.asctime())
print("----------------------------")

print("SILA MASUKKAN MAKLUMAT BERIKUT")
firstName = input("1>>Masukkan nama pertama anda :   ")  #NAMA PERTAMA
secondName = input("2>>Masukkan nama kedua anda :   ") #NAMA KEDUA

yob = int (input("3>>Masukkan tahun anda dilahirkan :   "))   # TAHUN DILAHIRKAN
option = int (input("4>>Masukkan pilihan umur utk pencen :   ")) #UMUR
umur=(2024-yob)
thnpencen=yob+option
bakiservis=thnpencen-2017

#PAPARAN MAKLUMAT DIRI DAN TARIKH BERSARAH
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("SELAMAT DATANG", firstName)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("MARI LIHAT UMUR PENCEN ANDA")

print(time.asctime()) #TARIKH TERKINI
print("------------------------------------------------")


print("Nama anda ialah : " ,firstName + " " + secondName )
print(" ")
print("Umur anda ialah : " ,umur )

if umur < 44:
    print(" Cikgu still muda lagi..... ")
else:
    print(" Cikgu berpengalaman....... ")

print(" ")
print("Anda akan berpencen pada : " ,thnpencen )
print("Baki servis anda dalam kerajaan ialah : " ,bakiservis )
print(" ")

print("TERIMA KASIH")
print("----------------------------------------")