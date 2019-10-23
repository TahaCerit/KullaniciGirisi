print("""
************************
KULLANICI GİRİŞ PROGRAMI
************************""")
print("""
*************************
Kullanıcı Kaydı Oluştur..
*************************""")

sys_kullanici_kaydi = input("Kullanıcı Adı :")
sys_parola_kaydı = input("Parola :")
print("""
**********************
Kaydınız Oluşturuluyor...
**********************""")

sys_kullanici = sys_kullanici_kaydi
sys_parola =sys_parola_kaydı

giris_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adınız:")
    parola = input("Parolanız:")
    if(kullanıcı_adı != sys_kullanici and parola == sys_parola):
        print("Kullanıcı Adınız Hatalı")
        giris_hakkı -=1
    elif(kullanıcı_adı == sys_kullanici and parola != sys_parola):
        print("Parolanız Hatalı")
        giris_hakkı -=1
    elif(kullanıcı_adı != sys_kullanici and parola != sys_parola):
        print("Kullanıcı Adınız ve Parolanız Hatalı")
        giris_hakkı -=1
    else:
        print("Başarıyla Giriş Yapıldı")
        break
    if(giris_hakkı ==0):
        print("Giriş Hakkınız Kalmadı...")
        break
