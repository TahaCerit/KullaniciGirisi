print("""
************************
Kullanıcı Giriş Programı
************************""")
sys_kullanici = "tahacerit"
sys_parola = "123456"

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
